from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('booked', 'Booked'), ('canceled', 'Canceled')])

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.TextField()  # Or create an Item model for detailed cart items

class Transaction(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
