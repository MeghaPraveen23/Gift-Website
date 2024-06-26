# Generated by Django 5.0.3 on 2024-04-14 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0002_cart'),
        ('gift_seller', '0003_remove_product_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('userinfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_app.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_app.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_seller.product')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('customize_name', models.CharField(max_length=100, null=True)),
                ('customize_desc', models.CharField(max_length=500, null=True)),
                ('customize_img', models.ImageField(upload_to='media')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_app.order')),
                ('userinfo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_app.userinfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
