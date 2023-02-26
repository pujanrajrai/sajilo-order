from django.shortcuts import render
from .forms import CustomerProfileForm,VendorProfileForm
# Create your views here.
from django.views.generic import CreateView,UpdateView
from .models import VendorProfile,CustomerProfile

class VendorProfileCreateView(CreateView):
    model = VendorProfile
    form_class = VendorProfileForm
    template_name = 'vendor_profile_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/profiles/view'


class CustomerProfileCreateView(CreateView):
    model = CustomerProfile
    form_class = CustomerProfileForm
    template_name = 'myprofile/profile_create_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return '/profiles/view'


