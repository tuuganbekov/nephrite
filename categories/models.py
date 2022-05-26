from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    sub_category = models.ForeignKey('Category', related_name='parent', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')

    def __str__(self) -> str:
        return self.title
        
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        