from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')