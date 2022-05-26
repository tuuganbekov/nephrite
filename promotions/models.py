from django.db import models

from products.models import Product

# Create your models here.
class Promotion(models.Model):
    title = models.CharField(max_length=250)
    product = models.ManyToManyField(Product, related_name="product_promotions")
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'        