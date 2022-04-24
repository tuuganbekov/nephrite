from django.contrib import admin
from products.models import Product


# Register your models here.
@admin.register(Product)
class StageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'old_price',
        'new_price',
        'quantity',
        'is_active',
        )
    search_fields = ('title',)
    list_filter = ('old_price', 'new_price',)