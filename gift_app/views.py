from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import UserInformation, Seller, Customization, purchases
from django.contrib.auth import authenticate, login
from gift_admin.models import Category
from gift_seller.models import Product
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{'categories': categories})

def loginview(request):
    if request.method=='POST':
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/adminhome')
            elif user.is_staff:
                return redirect('/sellerhome')
            else:
                return redirect('/home')

        else:
            messages.success(request,'Invalid Username or Password')
            return render(request, 'login.html')
    else:
         messages.success(request, 'You are now logged in.')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobilenumber = request.POST['mobilenumber']
        username = request.POST['name']
        password = request.POST['password']
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('sellereg')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('sellereg')
        else:
        # Create User
            seller = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
            seller.first_name = name
            seller.save()
            sellerinfo = Seller.objects.create(user=seller, name=name, email=email, password=password, mobilenumber=mobilenumber)
            sellerinfo.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
            
        return render(request,'sellereg.html')

def user_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobilenumber = request.POST['mobilenumber']
        housename = request.POST['housename']
        email = request.POST['email']
        username = request.POST['name']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name= name
            user.save()
            userinfo = UserInformation.objects.create(user=user, name=name, email=email, password=password, mobilenumber=mobilenumber, housename=housename)
            userinfo.save()

            # Log the user in after registration
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login') 
    else:
        return render(request,'signup.html')

def userhome(request):
    categories = Category.objects.all()
    return render(request, 'home.html',{'categories': categories})

def category_view(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_view.html', {'category': category, 'products': products})

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html',{'products': products})

def customize(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        message = request.POST.get('message')

        Customization.objects.create(
            name=name, 
            img=img, 
            message=message
        )
        return redirect('cart')
    return render(request, 'customize.html')
    
def success(request):
    return render(request, 'success.html')

def cart(request):
    carts=Product.objects.get(id=6)
    print(carts)
    return render(request, 'cart.html',{'carts':carts})

def orders(request):
    # Assuming user information is fetched correctly
    user_info = UserInformation.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        # Get data from the POST request
        product_name = request.POST.get('product')
        total_item = request.POST.get('total_item')
        total_price = request.POST.get('total_price')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')

        try:
            # Fetch the product instance based on the product name
            product = Product.objects.get(name=product_name)
            
            # Create a new purchases object with the fetched product instance
            purchase = purchases.objects.create(
                user=user_info,
                product=product,
                total_item=total_item,  # Ensure that total_item is provided
                total_price=total_price,
                card_name=card_name,
                card_number=card_number
            )

            # Optionally, redirect to a success page
            return redirect('success')
        except Product.DoesNotExist:
            return HttpResponse("Product with the given name does not exist.")

    purchase = purchases.objects.get(id=6)
    return render(request, 'orders.html',{'purchase':purchase})