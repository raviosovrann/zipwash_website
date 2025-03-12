from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('about', views.about, name='about'),
]