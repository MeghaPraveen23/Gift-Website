from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=8)

class UserInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    housename = models.CharField(max_length=200)
    mobilenumber = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=8)

class Customization(models.Model):  # Renamed to singular form
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Cart(models.Model):
    from gift_seller.models import Product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models

class purchases(models.Model):
    from gift_seller.models import Product
    user=models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    total_item=models.CharField(max_length=150)
    total_price=models.CharField(max_length=150)
    card_name=models.CharField(max_length=150)
    card_number=models.FloatField(max_length=150)
    cvv=models.CharField(max_length=150)
    status=models.CharField(max_length=150)