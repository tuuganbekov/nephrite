from distutils.command.upload import upload
from pydoc import describe
from unicodedata import category
from django.db import models

from categories.models import Category


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    old_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    new_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='products')
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
        