# Generated by Django 5.0.3 on 2024-04-17 06:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0005_remove_cart_product_remove_cart_quantity_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
