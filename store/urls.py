from django.urls import path 
from django.urls.conf import include
from django.contrib import admin
from django.urls import path, include

from rest_framework_nested import routers
from . import views




from . import views
from pprint import pprint


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename='carts')
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet,  basename='orders') # changed this to basename because we have no queryset defined in the viewset


products_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
products_router.register('images', views.ProductImageViewset, basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup = 'cart') # this giveus a url called cart/pk
carts_router.register('items', views.CartItemViewset, basename='cart-items')




urlpatterns = router.urls + products_router.urls + carts_router.urls

