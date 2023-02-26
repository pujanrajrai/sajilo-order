from django.contrib import admin
from .models import *
from profiles.models import CustomerProfile,VendorProfile
# Register your models here.
admin.site.register(EmailVerification)
admin.site.register(CustomUser)
admin.site.register(CustomerProfile)
admin.site.register(VendorProfile)