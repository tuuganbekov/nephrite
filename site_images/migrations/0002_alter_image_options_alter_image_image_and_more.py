# Generated by Django 4.0.4 on 2022-04-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_type',
            field=models.IntegerField(choices=[(1, 'Логотип'), (2, 'Баннер')], default=1, verbose_name='Тип картинки'),
        ),
        migrations.AlterField(
            model_name='image',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активный'),
        ),
    ]
