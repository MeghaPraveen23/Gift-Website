from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from gift_admin.models import Category
from django.urls import reverse

# Create your views here.
def adminhome(request):
    users = User.objects.all()
    categories = Category.objects.all()
    return render(request, 'admin/adminhome.html',{'categories':categories,'users':users})

def user(request):
    users = User.objects.all()
    return render(request, 'admin/users.html',{'users':users})

def addcategory(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name') 
        category_img = request.FILES.get('category_img')

        # Save the category details to the database
        category = Category.objects.create(
            category_name=category_name,
            category_img=category_img
        )

        # Redirect to a success page or another appropriate URL
        return redirect('addcategory')# Replace 'success_page' with the desired URL name or path
    
    return render(request, 'admin/addcategory.html')