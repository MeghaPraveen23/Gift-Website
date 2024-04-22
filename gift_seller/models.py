from django.db import models
from gift_admin.models import Category

# Create your models here.
class Product(models.Model):
    from gift_app.models import Seller
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(default=0)
    img = models.ImageField(upload_to='media')  # Assumes you have an 'uploads' folder in your MEDIA_ROOT
    
    def __str__(self):
        return self.name