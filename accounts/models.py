from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=255)
    shop_url = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.shop_name
