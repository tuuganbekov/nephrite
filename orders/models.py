from django.db import models

from products.models import Product


DELIVERY_TYPE = (
    (1, "Доставка по адресу"),
    (2, "Самовывоз")
)

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phone = models.TextField(max_length=250)
    email = models.CharField(max_length=250)
    total_sum = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    delivery = models.IntegerField(choices=DELIVERY_TYPE, default=1)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.address}"


class Order_product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.product} - {self.quantity}"
