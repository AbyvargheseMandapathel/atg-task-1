from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    

    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_city = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=100, blank=True, null=True)
    address_pincode = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username