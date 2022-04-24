from django.contrib import admin
from categories.models import Category


# Register your models here.
@admin.register(Category)
class StageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'sub_category',
        )
    search_fields = ('title',)
    