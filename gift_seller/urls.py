from django.urls import path
from.import views 

urlpatterns = [
    path('sellerhome',views.sellerhome,name="sellerhome"),
    path('addproduct',views.addproduct,name="addproduct"),
]