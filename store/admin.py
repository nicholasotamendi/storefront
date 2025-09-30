from django.contrib import admin, messages
from django.db.models import Count
from django.urls import reverse 
from django.utils.html import format_html, urlencode 
from django.utils.translation import ngettext
from django.contrib.contenttypes.admin import GenericTabularInline

from . import models 




#creating custom filters
class InventoryFilter(admin.SimpleListFilter):
    title = 'Inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt = 10)
        
    


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail" />')
        return ''


# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collections']
    prepopulated_fields = {
        'slug':['title']
    }
    exclude = ['promotions']
    actions = ['clear_inventory']
    inlines = [ProductImageInline]
    list_display = ['title', 'unit_price', 'collections', 'inventory_status',]
    list_editable = ['unit_price']
    list_filter =['collections','last_update', InventoryFilter]
    search_fields = ['title']
    list_per_page = 10
    #adding computed column 

    #newly added
    def collection_title(self, product):
        return product.collection.title
    
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'
    
    #defining custom actions
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} product(s) were successfully updated',
            messages.ERROR
        )

    class Media:
        css = {
            'all': ['store/styles.css']
        } #this is how to add custom css to the admin panel and link it to the static folder
        

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']
    list_per_page = 10
    #this is how to setup a new product with a foreign key feature and link it to the product

    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({'collections__id': str(collection.id)})
        )
        count = collection.products.count()
        return format_html('<a href="{}">{}</a>', url, count)

    products_count.admin_order_field = 'products_count'


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )



'''@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10

    def orders_count(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            })
        )
        return format_html('<a href = "{}">{}</a>', url, customer.orders_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )'''


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    list_filter = ['membership']


    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')   # or 'orders' if you set related_name
        )

    def orders_count(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({'customer__id': str(customer.id)})
        )
        text = ngettext(
            '%(count)d order',
            '%(count)d orders',
            customer.orders_count
        ) % {'count': customer.orders_count}
        return format_html('<a href="{}">{}</a>', url, text)

    orders_count.admin_order_field = 'orders_count'


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    min_num = 1
    max_num = 10
    extra = 1




@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = [ 'id', 'customer', 'placed_at', 'payment_status']
    list_per_page = 10
    list_select_related = ['customer']
    list_filter = ['placed_at', 'payment_status']






