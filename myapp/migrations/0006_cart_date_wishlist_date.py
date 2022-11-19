# Generated by Django 4.0.4 on 2022-07-07 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
