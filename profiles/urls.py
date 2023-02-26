from django.urls import path,include
from . import views
app_name="profiles"
urlpatterns = [
    path('customer/create',views.CustomerProfileCreateView.as_view(),name="customer_create"),
    path('vendor/create',views.VendorProfileCreateView.as_view(),name="venodr_create"),
]
