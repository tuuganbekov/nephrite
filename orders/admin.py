from django.contrib import admin
from orders.models import Order, Order_product

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'address',
        'total_sum',
        'delivery',
        )
    search_fields = ('full_name', 'delivery', 'address', 'phone', 'email',)
    list_filter = ('delivery',)


@admin.register(Order_product)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'quantity',
        'total_price',
        )
    search_fields = ('product',)
