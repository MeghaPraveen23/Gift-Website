from django.urls import path
from.import views 

urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.loginview,name="login"),
    path('sellereg',views.register,name="sellereg"),
    path('signup',views.user_registration,name='signup'),
    path('home',views.userhome,name="home"),
    path('category/<int:category_id>/', views.category_view, name='category_view'),
    path('products',views.products,name="products"),
    path('cart/',views.cart,name="cart"),
    path('customize',views.customize,name="customize"),
    path('cart/orders',views.orders,name="orders"),
    path('success',views.success,name="success"),
]

