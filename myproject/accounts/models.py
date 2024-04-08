from django.db import models
from django.contrib.auth.models import User

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resident')
    # Add other fields specific to residents

    lname = models.CharField(max_length=50, null=True, blank=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')
    # Add other fields specific to admins
    lname = models.CharField(max_length=50, null=True, blank=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
