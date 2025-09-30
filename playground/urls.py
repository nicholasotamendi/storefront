from django.urls import include, path 
from . import views

#urlconf module

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
]
