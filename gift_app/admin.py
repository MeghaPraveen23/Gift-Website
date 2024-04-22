from django.contrib import admin
from .models import Seller, UserInformation, Customization, purchases

# Register your models here.
admin.site.register(Seller)
admin.site.register(UserInformation)
admin.site.register(Customization)
admin.site.register(purchases)