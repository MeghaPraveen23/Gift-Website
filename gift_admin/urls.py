from django.urls import path
from.import views 

urlpatterns = [
    path('adminhome',views.adminhome,name="adminhome"),
    path('users',views.user,name="users"),
    path('addcategory',views.addcategory,name="addcategory"),
]