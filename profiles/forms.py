from django import forms
from .models import CustomerProfile,VendorProfile

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model=VendorProfile
        fields=[
            "company_name","company_description",
            "company_address","company_phone"
            ]

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerProfile
        fields = [
            "address",
            "phone",
            "photo"
        ]
        widget={
            
        }