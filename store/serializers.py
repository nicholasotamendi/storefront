from rest_framework import serializers
from .models import Product, Collection, ProductImage, Review, Cart, CartItem, Customer, Order, OrderItem

from django.db import transaction

from decimal import Decimal

from .signals import order_created


#serializers convert model instances to a dictionary 

# Collection Serializer
class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only = True)
    class Meta:
        model = Collection
        fields = [
            'id',
            'title',
            'products_count'
        ]
    


    def get_products_count(self, collection):
        return collection.products.count()


# Product Image Serializer
class ProductImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id = product_id, **validated_data) #this line creates a new ProductImage instance
    # **validated_data unpacks the dictionary into keyword arguments


    class Meta:
        model = ProductImage
        fields = [
            'id',
            'image'
        ]
    
# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many = True, read_only = True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'slug',
            'inventory',
            'description',
            'unit_price',
            'price_with_tax',
            'collections' ,
            'images'
        ]
    #avoid this practice fields = '__all__' as it exposes all sensitive informations 

    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length = 255)
    #description = serializers.CharField(max_length = 255)
    #price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    #collection = CollectionSerializer()
    '''colection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection-detail'
    )
    '''

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.075)
    
    '''
    def create(self, validated_data):
        product = Product(**validated_data)
        product.other = 1
        product.save()
        return product 
    
    def update(self, instance, validated_data):
        instance.unit_price = validated_data.get('unit_price')
        instance.save()
        return instance
        '''
    
    '''
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            return serializers.ValidationError('Passwords do not match')
        return data'''
    


#To create APIs
#firstly, create a model, make migrations, then migrate 
#secondly, create a serializer class, create a view, then register a route 

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'date',
            'name',
            'description'
        ]

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)
    
# Cart Serializer
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'unit_price'

        ]

# Update Cart Item Serializer
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'quantity'
        ]
    

# Add Cart Item Serializer
class AddCartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('No Product with the given ID was found')
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id = cart_id, product_id = product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            #create a new item 
            self.instance = CartItem.objects.create(cart_id = cart_id, **self.validated_data)

        return self.instance

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product_id',
            'quantity'
        ]

# Cart Item Serializer
class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart_item: CartItem):
        total_price = cart_item.quantity * cart_item.product.unit_price 
        return total_price 

    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity',
            'total_price'
        ]

# Cart Serializer
class CartSerialzer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many = True, read_only = True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, cart: Cart):
        total_list = sum([item.quantity * item.product.unit_price for item in cart.items.all()])
        return total_list


    class Meta:
        model = Cart
        fields = [
            'id',
            'items',
            'total_price'
        ]
        
# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Customer
        fields = [
            'id',
            'user_id',
            'phone',
            'birth_date',
            'membership'
        ]

# Order Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'quantity',
            'unit_price'
        ]

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True, read_only = True)
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'placed_at',
            'payment_status',
            'items'
        
        ]
        read_only_fields = ['id', 'placed_at']

# Update Order Serializer
class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'payment_status'
        ]

# Create Order Serializer
class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    
    #this validates if the cart exists and is not empty 
    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk = cart_id).exists():
           raise serializers.ValidationError('No cart with the given ID was found')
        if CartItem.objects.filter(cart_id = cart_id).count() == 0:
            raise serializers.ValidationError('The cart is empty')
        return cart_id

    

    def save(self, **kwargs):
        with transaction.atomic(): #this ensures that all the operations inside this block are executed as a single transaction
            cart_id = self.validated_data['cart_id']
            customer = Customer.objects.get(user_id = self.context['user_id'])
            order = Order.objects.create(customer = customer)
            
            cart_items = CartItem.objects\
                .select_related('product')\
                .filter(cart_id = cart_id)
            
            order_items = [OrderItem(
                order = order,
                product = item.product,
                quantity = item.quantity,
                unit_price = item.product.unit_price
            ) for item in cart_items
            ]

            OrderItem.objects.bulk_create(order_items) #insert all order items at once in bulk

            Cart.objects.filter(pk = cart_id).delete() # helps to clear the cart once the order is placed

            order_created.send_robust(self.__class__, order = order) #send the signal after the order is created
            #self.__class__ is used to indicate the sender of the signal, which in this case is the CreateOrderSerializer class itself
            return order
        

