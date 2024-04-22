from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from gift_seller.models import Product
from gift_admin.models import Category
from gift_app.models import Seller
from django.urls import reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def sellerhome(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'seller/sellerhome.html',{'products':products,'categories':categories})

def addproduct(request):
    try:
        # Attempt to retrieve the seller object based on the user's ID
        seller = Seller.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        # Handle the case where the seller does not exist
        return HttpResponse("Seller does not exist.")

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price') 
        img = request.FILES.get('img')
        category = request.POST.get('category')

        # Check if the category exists
        try:
            category = Category.objects.get(id=category)
        except Category.DoesNotExist:
            # Handle the case where the category does not exist
            return HttpResponse("Category does not exist.")
        
        # Save the product details to the database
        product = Product.objects.create(
            seller=seller,
            name=name,
            price=price,
            img=img,
            category=category,
        )
        # Redirect to a success page or another appropriate URL
        return redirect('addproduct')  # Replace 'addproduct' with the desired URL name or path
    else:
        categories = Category.objects.all()
        return render(request, 'seller/addproduct.html', {'categories': categories})