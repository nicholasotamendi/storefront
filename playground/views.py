from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView as apiView
from django.utils.decorators import method_decorator

from django.core.cache import cache

import requests

from .tasks import notify_customers

from tags.models import TaggedItems

from store.models import Product, OrderItem, Collection, Customer, Order

import logging 
# Create your views here.

# A view is a request handler (takes a request and returns a response)

logger = logging.getLogger(__name__) 

'''
def say_hello(request):
    queryset = Product.objects.filter(unit_price__range=(20, 30))

    return render(request, 'hello.html',
                  {'name': 'Jacinth', 'products': queryset})

'''

#class based view of say_hello view
class HelloView(apiView):
    @method_decorator(cache_page(5 * 60)) #method decorator to cache the view for 5 minutes, method decorators are used to decorate class based views
    def get(self, request):
        try: 
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2') #this will make a get request to the url and wait for 2 seconds before returning a response
            logger.info('Received the response')
            data = response.json()
        except request.ConnectionError:
            logger.critical('httpbin is offline')

        return render(request, 'hello.html', {'name': data})
    


#function based view with caching of say_hello view
'''
@cache_page(5 * 60) #cache the view for 5 minutes
def say_hello(request):

    #Expression wrapper 
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    discount = Product.objects.annotate(
        discounted_price = discounted_price
    )

    response = requests.get('https://httpbin.org/delay/2') #this will make a get request to the url and wait for 2 seconds before returning a response
    data = response.json()

    return render(request, 'hello.html',
                  {'name': data, 
                   'discount': discount,
                   })
'''
#NB: cache decorators would not work with class based views


    #queryset = Product.objects.filter(last_update__year=2025)
    # find all products with inventory < 10 and unit price < 20
    #queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # using Q objects Q objects encapsulate each keyword argument in a separate object
    #queryset = Product.objects.filter(
    #    Q(inventory__lt=10) | ~Q(unit_price__lt=20)
    #)   

    #referencing fields using F objects
    #find all products where the inventory equals the unit price
    #queryset = Product.objects.filter(inventory__lte=F('unit_price'))


    #sorting data using order_by
    #queryset = Product.objects.order_by('-unit_price', '-title')
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')

    #limiting querysets using array slicing syntax
    #queryset = Product.objects.all()
    #queryset = Product.objects.select_related('collection').all()
    #queryset = Product.objects.prefetch_related('promotions').all()[:10]



    #qeurying related objects
    #queryset = Product.objects.values('id', 'title', 'collection__title')

    #select products that have been ordered and sort them by their title
    #orderset = OrderItem.objects.values('product_id')
    #contigo = Product.objects.filter(id__in = orderset).order_by('title')[:10]

    # select related and prefetch related 
    #elcamino = Order.objects.select_related('customer').prefetch_related('orderitem_set').order_by('-customer_id')[:5]

    #aggregate
    #result = Product.objects.aggregate(count = Count('id'), min_price = Min('unit_price'))

    #annotate
"""    
    newcust = Customer.objects.annotate(full_name = Func(
        F('first_name'),
        Value(' '),
        F('last_name'),
        function = 'CONCAT'
    ))
"""

    #newcust = Customer.objects.annotate(full_name = Concat('first_name', Value(' ') ,'last_name'))

    #grouping data 



    # this is how to get the tags for a given product
'''content_type = ContentType.objects.get_for_model(Product) #this finds content type id for us 
    itemset = TaggedItems \
    .objects.select_related('tag') \
    .filter(
        content_type = content_type,
        object_id = 1
    )
'''
    #itemset = TaggedItems.objects.get_tags_for(Product, 1)
    

    #creating objects - insterting records into the db 
'''
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk = 1)
    collection.save()    
'''

    #updating the records
    #always get the objects first from the db before updating it (read it first)
'''
    collection = Collection.objects.get(pk = 101)
    collection.title = 'Games'
    collection.featured_product = Product(pk = 2)
    collection.save()
'''

    #Collection.objects.filter(pk = 11).update(featured_product=None)

    #Deleting multiple objects 
    #Collection.objects.filter(id__gt = 5),delete()

    #transactions (atomic way and rollback)
'''with transaction.atomic():

        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 25
        item.unit_price = 19
        item.save()'''
'''
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, title' \
        ' FROM store_product')
        cursor.callproc('get_customers', [1,2,3])'''
'''Product.objects.raw(
        'SELECT id, title' \
        ' FROM store_product'
    )
'''
'''    #this is how to send email in django using django core email
    try:
        email = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Jacinth'}
        )
        email.send(['recipient@example.com'])

    except BadHeaderError:
        pass
'''
        
    #notifications = notify_customers.delay('Hello Customers!') #this will run the task in the background using celery


    #queryset = Product.objects.only('id','title') - only returns id and title
    #queryset = Product.objects.defer('description') - returns all fields except description

    #requests.get('https://httpbin.org/delay/2') #this will make a get request to the url and wait for 2 seconds before returning a response


    #caching example
''' key = 'httpbin_result'
    if cache.get(key) is None: #check if the result is already in the cache
        response = requests.get('https://httpbin.org/delay/2') #this will make a get request to the url and wait for 2 seconds before returning a response
        data = response.json()
        cache.set(key, data) #cache the result for 30 seconds
'''


    #caching example with decorator

'''counters = Customer.objects.annotate(
        orders_count = Count('order')
    )
    '''