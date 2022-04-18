# Generated by Django 4.0.4 on 2022-04-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='media/products/')),
                ('description', models.TextField()),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('new_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]