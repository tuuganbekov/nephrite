from django.contrib import admin
from orders.models import Order, Order_product
from django.utils.html import format_html

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone',
        'address',
        'total_sum',
        'delivery',
        'order_products',
        )
    search_fields = ('full_name', 'delivery', 'address', 'phone', 'email', )
    list_filter = ('delivery',)

    def order_products(self, obj):
        return format_html(f"<a href='/admin/orders/order_product/?order__id={obj.id}'>Продукты заявки</a>")

    order_products.short_description = "Продукты"


@admin.register(Order_product)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'order',
        'quantity',
        'total_price',
        )
    list_filter = ('product', 'order__full_name',)
