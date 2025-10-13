from django.urls import include, path 
from . import views

#urlconf module

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='say_hello'),
]
