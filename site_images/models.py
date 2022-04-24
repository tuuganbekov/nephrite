from distutils.command.upload import upload
from django.db import models


IMAGE_TYPE = (
    (1, 'Логотип'),
    (2, 'Баннер')
)

# Create your models here.
class Image(models.Model):
    image_type = models.IntegerField(choices=IMAGE_TYPE, default=1)
    image = models.ImageField(upload_to='media/')
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        image_type_dict = dict(IMAGE_TYPE)
        return image_type_dict[self.image_type]