from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')

def pricing(request):
    return render(request, 'pricing.html')

def about(request):
    return render(request, 'about.html')
