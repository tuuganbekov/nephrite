# Generated by Django 4.0.4 on 2022-04-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type', models.IntegerField(choices=[(1, 'Логотип'), (2, 'Баннер')], default=1)),
                ('image', models.ImageField(upload_to='media/')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
