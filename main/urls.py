from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user_view/', views.user_view, name='user_view'),
    path('vendor_view/', views.vendor_view, name='vendor_view'),
]