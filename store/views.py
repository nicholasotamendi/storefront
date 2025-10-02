from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from .models import Product, Collection, OrderItem, ProductImage, Review, Cart, CartItem, Customer, Order
from .serializers import OrderSerializer, ProductImageSerializer, ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerialzer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer, CustomerSerializer, CreateOrderSerializer, UpdateOrderSerializer
from .filters import ProductFilter
from .pagination import DefaultPagination

from .permissions import IsAdminOrReadOnly, FullDjangoModelPermissions, ViewCustomerHistoryPermission


# Create your views here.

#a view function takes a request and returns a response 
#class based views help us write clean codes

class ProductViewSet(ModelViewSet):

    queryset = Product.objects.prefetch_related('images', 'collections').all()
    #using generic filtering (browsable API)
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    #implementing searching in browsable APIs
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']

    '''
    def get_queryset(self):
        queryset = Product.objects.all()
        collections_id = self.request.query_params.get('collections_id')
        if collections_id is not None:
           queryset = queryset.filter(collections_id=collections_id)

        return queryset
    '''
        #return Product.objects.filter(collection_id = self.request.query_params['collecton_id'])
    
    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if OrderItem.objects.filter(product_id = pk).count() > 0:
            return Response({'error': 'Product cannot be deleted because it is assocaited with an order item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)       
        return super().destroy(request, *args, **kwargs)
    
    '''    
        def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)      
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is assocaited with an order item'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
        '''   

'''class ProductList(ListCreateAPIView):
    #the generic view helps us in browsable APIs to get a HTML form for posting entries into the db
    queryset = Product.objects.select_related('collections').all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}'''
    
    #this is the way to create this using APIView inherited (class ProductList(APIView))
'''    
    def get(self, request): 
        queryset = Product.objects.select_related('collections').all()
        serializer = ProductSerializers(
            queryset,
            many = True,
            context = {'request': request}
            )
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)'''

#function based
'''
#function way of building views
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method =='GET':
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset, many=True, context = {
        'request':request
        })
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
'''
'''try:
            product = Product.objects.get(pk=id)
            serializer = ProductSerializers(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
    '''
'''
class ProductDetail(RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #lookup_field = 'id' to force django to use id instead of pk

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk) 
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is assocaited with an order item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
'''  
    
'''    
    def get(self, request, id):`
        product = get_object_or_404(Product, pk=id) 
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id) 
        serializer = ProductSerializer(product, data = request.data) # we pass a product instance so the serializer can update that certain product
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''
# function based
'''@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializers(product, data = request.data) # we pass a product instance so the serializer can update that certain product
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if product.orderitems.count() > 0:
            return Response({'error': 'Product cannot be deleted because it is assocaited with an order item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

#serializers convert model instances to a dictionary 

class CollectionViewSet(ModelViewSet):
    queryset = queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request} 

    def destroy(self, request, *args, **kwargs):
        collection = self.get_object()
        if collection.products.count()>0:
            return Response({'error': 'Collection cannot be deleted because it is assocaited with a product item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

    ''' 
    def delete(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
        products_count = Count('products')
        ), pk = pk)
        if collection.products.count()>0:
            return Response({'error': 'Collection cannot be deleted because it is assocaited with a product item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''

'''
class CollectionList(ListCreateAPIView):
    queryset = queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request': self.request}'''


# this is used for class CollectionList(APIView)
'''    def get(self, request):
        queryset = Collection.objects.annotate(products_count = Count('products')).all()
        serializer = CollectionSerializer(queryset, many = True, context = {
            'request': request
        })
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CollectionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)'''

# FUNCTION BASED
'''
@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count = Count('products')).all()
        serializer = CollectionSerializer(queryset, many = True, context = {
            'request': request
        })
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)'''

'''class CollectionDetail(RetrieveUpdateDestroyAPIView):

    queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
        products_count = Count('products')
        ), pk = pk)
        if collection.products.count()>0:
            return Response({'error': 'Collection cannot be deleted because it is assocaited with a product item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


'''def get(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
        products_count = Count('products')
        ), pk = pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    
    def put(self, request, pk):
        collection = get_object_or_404(Collection.objects.annotate(
        products_count = Count('products')
        ), pk = pk)
        serializer = CollectionSerializer(collection, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
''' 
    

# fucntion based
'''
@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection.objects.annotate(
        products_count = Count('products')
    ), pk = pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if collection.products.count()>0:
            return Response({'error': 'Collection cannot be deleted because it is assocaited with a product item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk']).all()
        #self.kwargs helps us to access the parameters in the url pattern

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

# Four ways to serialize relationships 
#- Primary Key 
#- String
#- Nested Objects
#- Hyperlink

class CartViewSet(CreateModelMixin, 
                  GenericViewSet, 
                  RetrieveModelMixin, 
                  DestroyModelMixin):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerialzer


class CartItemViewset(ModelViewSet):

    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}


    #serializer_class = CartItemSerializer
    def get_queryset(self):
        return CartItem.objects.filter(
            cart_id = self.kwargs['cart_pk']
        ).select_related('product')
    

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser] # setting permsission at the view level

    @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])  # this determine whether it is availavle in customers/me or customers/1/me
    def history(self, request, pk):
        return Response('ok')

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])  # this determine whether it is availavle in customers/me or customers/1/me
    def me(self, request):
        customer_id = request.user.id
        customer = Customer.objects.get(user_id = customer_id) #this is used to unpack the tuple from get or create before passing it to the serializer
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data) 
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
    
class OrderViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    # this helps to set different permissions for different methods in the same viewset
    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]


    def create(self, request, *args, **kwargs):
        serializer = CreateOrderSerializer(data = request.data, context = {'user_id': self.request.user.id})
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()

        customer = Customer.objects.only('id').get(user_id = user.id)
        return Order.objects.filter(customer = customer)



#in django signals are used to decouple different parts of the application
#signals allow certain senders to notify a set of receivers when some action has taken place

class ProductImageViewset(ModelViewSet):

    serializer_class = ProductImageSerializer

    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs['product_pk'])
        #self.kwargs helps us to access the parameters in the url pattern

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
        #this helps us to pass the product id to the serializer so that we can use it to create a product image instance    

    
