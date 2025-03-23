from django.db import models

# Create your models here.

class ServiceCategory(models.Model):
    """
    Represents a category of services.

    Attributes:
        name (str): The name of the service category.
        description (str): A brief description of the service category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name

class Service(models.Model):
    """
    Represents a service offered by the company.

    Attributes:
        category (ServiceCategory): The category to which the service belongs.
        name (str): The name of the service.
        description (str): A brief description of the service.
        price (Decimal): The price of the service.
        image (ImageField): An optional image of the service.
    """
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Services"
        ordering = ['name']

    def __str__(self):
        return self.name

class ServiceBooking(models.Model):
    """
    Represents a booking for a service.

    Attributes:
        service (Service): The service that is booked.
        user (User): The user who booked the service.
        booking_date (datetime): The date and time when the booking was made.
        status (str): The status of the booking (e.g., booked, completed).
    """
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('completed', 'Completed')], default='booked')

    class Meta:
        verbose_name_plural = "Service Bookings"
        ordering = ['-booking_date']

    def __str__(self):
        return f"{self.service.name} booked by {self.user.username}"

class ServiceCompletion(models.Model):
    """
    Represents the completion of a booked service.

    Attributes:
        booking (ServiceBooking): The booking that was completed.
        completion_date (datetime): The date and time when the service was completed.
        feedback (str): Optional feedback provided by the user.
    """
    booking = models.OneToOneField(ServiceBooking, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Service Completions"
        ordering = ['-completion_date']

    def __str__(self):
        return f"{self.booking.service.name} completed on {self.completion_date}"