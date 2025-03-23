from django.contrib import admin
from .models import Service, ServiceCategory, ServiceBooking, ServiceCompletion

# Register your models here.
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(ServiceBooking)
admin.site.register(ServiceCompletion)