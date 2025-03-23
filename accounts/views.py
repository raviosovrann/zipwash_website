from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm
from .models import Customer, Vendor

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if hasattr(user, 'vendor'):
                    return redirect('accounts:vendor_profile')
                else:
                    return redirect('accounts:customer_profile')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            if form.cleaned_data['is_vendor']:
                Vendor.objects.create(user=user, email=user.email, first_name=request.POST['first_name'], last_name=request.POST['last_name'], shop_name=request.POST['shop_name'], shop_url=request.POST['shop_url'], phone_number=request.POST['phone_number'])
            else:
                Customer.objects.create(user=user, email=user.email)
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                if form.cleaned_data['is_vendor']:
                    return redirect('accounts:vendor_profile')
                else:
                    return redirect('accounts:customer_profile')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def customer_profile(request):
    return render(request, 'accounts/customer_profile.html')

@login_required
def vendor_profile(request):
    return render(request, 'accounts/vendor_profile.html')

def logout(request):
    auth_logout(request)
    return redirect('services:home')