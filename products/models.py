from tabnanny import verbose
from django.db import models

from categories.models import Category


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(upload_to='media/', verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание')
    old_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Старая цена')
    new_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Новая цена')
    quantity = models.IntegerField(null=True, blank=True, verbose_name='Количество')
    category = models.ManyToManyField(Category, related_name='products', verbose_name='Продукты')
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        