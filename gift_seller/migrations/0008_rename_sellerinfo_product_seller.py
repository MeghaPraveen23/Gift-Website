# Generated by Django 5.0.3 on 2024-04-18 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift_seller', '0007_alter_product_sellerinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sellerInfo',
            new_name='seller',
        ),
    ]