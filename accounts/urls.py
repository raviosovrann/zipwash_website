from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
    path('vendor_profile/', views.vendor_profile, name='vendor_profile'),
    path('logout/', views.logout, name='logout'),  
]
