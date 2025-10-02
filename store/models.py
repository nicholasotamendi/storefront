from django.db import models
from django.core.validators import MinValueValidator
from django.contrib import admin

from django.conf import settings

from uuid import uuid4

from store.validators import validate_file_size

# Create your models here.
# A model is a special kind of object - it maps to a single database table
# this data model will be for an e-commerce application 
# we will use models ustomer, Product, Collection, Order, OrderItem, Cart, Tag

# there is a manytomany relationship between products and cart with an attribute called "CartItem". Cart Item is an association model that links products and carts together.
# customer has a onetomany relation with Order
# Product has a manytomany relation with Order through OrderItem

# there is a manytomany relationship between products and tags using TagItem
# the ability to tag products is optional and will be added to a new app called Tags and import it 


# Create your models here.

#promotion class 
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

#collection class
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

#product class 
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(null = True, blank = True)
    unit_price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        validators=[MinValueValidator(1)])
    inventory = models.IntegerField(validators=[MinValueValidator(1)])
    last_update = models.DateTimeField(auto_now=True)
    #collections = models.ManyToManyField(Collection, related_name='products')
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    promotions = models.ManyToManyField(Promotion, related_name='products', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='store/images', validators=[validate_file_size])

    def __str__(self):
        return f"Image for {self.product.title}"


#customer class
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    #first_name = models.CharField(max_length=60)
    #last_name = models.CharField(max_length=60)
    #email = models.EmailField(unique=True)
    phone = models.CharField(max_length=60, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #membership field is a choice field
    membership = models.CharField(max_length=1, choices=
                                  MEMBERSHIP_CHOICES,
                                    default=MEMBERSHIP_BRONZE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @admin.display(ordering ='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering ='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]



# Order class
class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETED, 'Completed'),
        (PAYMENT_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_PENDING)

    #creating custom permissions
    class Meta:
        permissions = [
            ('cancel_order','Can cancel order')
        ]

    def __str__(self):
        return f"Order {self.id} by {self.customer}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.SmallIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

# Cart class
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"

# CartItem class
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators= [MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]

    def __str__(self):
        return f"{self.quantity} of {self.product.title} in Cart {self.cart.id}"

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=255, blank=True)  

    def __str__(self):
        return f"{self.street}, {self.city}"
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


#object relational mapping (ORM) - a technique that lets you query and manipulate data from a database using an object-oriented paradigm.
# Django's ORM allows you to define your data models as Python classes, and it automatically translates these classes into database tables.
# Each attribute of the class represents a database field in the table.

#create mock data for models: Product, Collection, Customer, Order, OrderItem, Cart, CartItem, Address, Promotion
# use Django's built-in admin interface to add, edit, and delete records in the database

