from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_img = models.ImageField(upload_to='media')  # Assumes you have an 'uploads' folder in your MEDIA_ROOT
    
    def __str__(self):
        return self.category_name