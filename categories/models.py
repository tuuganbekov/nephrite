from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    sub_category = models.ForeignKey('Category', related_name='parent', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
        
    class Meta:
        verbose_name_plural = 'Categories'
        