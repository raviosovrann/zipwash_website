from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User, Vendor, Customer

# Create your views here.

def home(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        first_name = request.POST['fname']
        last_name = request.POST['lname']

        # Create user with first_name and last_name
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        if role == 'seller':
            shop_name = request.POST['shopname']
            shop_url = request.POST['shopurl']
            phone = request.POST['phone']
            Vendor.objects.create(user=user, shop_name=shop_name, shop_url=shop_url, phone=phone)
            return redirect('vendor_view')
        else:
            Customer.objects.create(user=user)
            return redirect('user_view')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Attempting to authenticate user: {username}")
        user = authenticate(request, email=username, password=password)
        if user is not None:
            print(f"User authenticated: {user}")
            auth_login(request, user)
            if hasattr(user, 'vendor'):
                return redirect('vendor_view')
            else:
                return redirect('user_view')
        else:
            print("Authentication failed")
    return render(request, 'login.html')


def user_view(request):
    return render(request, 'user_view.html')


def vendor_view(request):
    return render(request, 'vendor_view.html')