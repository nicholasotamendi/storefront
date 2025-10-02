from django.db import models

# Create your models here.
# A model is a special kind of object - it maps to a single database table
# this data model will be for an e-commerce application 
# we will use models ustomer, Product, Collection, Order, OrderItem, Cart, Tag

# there is a manytomany relationship between products and cart with an attribute called "CartItem". Cart Item is an association model that links products and carts together.
# customer has a onetomany relation with Order
# Product has a manytomany relation with Order through OrderItem

# there is a manytomany relationship between products and tags using TagItem
# the ability to tag products is optional and will be added to a new app called Tags and import it 
