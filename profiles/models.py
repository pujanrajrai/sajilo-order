from django.db import models
from accounts.models import CustomUser
# Create your models here.

class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor_profile')
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    company_address = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    # company_email = models.EmailField()
    photo = models.ImageField(upload_to='vendor_photos/', blank=True, null=True)

class CustomerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='customer_photos/', blank=True, null=True)