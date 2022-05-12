from django.db import models

from products.models import Product


DELIVERY_TYPE = (
    (1, "Доставка по адресу"),
    (2, "Самовывоз")
)

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    phone = models.TextField(max_length=250, verbose_name='Телефон')
    email = models.CharField(max_length=250, verbose_name='Почта')
    total_sum = models.PositiveBigIntegerField(verbose_name='Итоговая стоимость')
    delivery = models.IntegerField(choices=DELIVERY_TYPE, default=1, verbose_name='Доставка')
    delivered = models.BooleanField(default=False, verbose_name='Доставлено')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    extra_info = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация')

    def __str__(self) -> str:
        return f"{self.full_name} - {self.address}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Order_product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    total_price = models.PositiveBigIntegerField(verbose_name='Сумма')

    def __str__(self) -> str:
        return f"{self.product} - {self.quantity}"

    class Meta:
        verbose_name = 'Продукт заявки'
        verbose_name_plural = 'Продукты заявки'
