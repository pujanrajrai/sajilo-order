from django.urls import path
from . import views

urlpatterns = [
    #admin product crud
    path('admin/create/',views.CreateProductView.as_view(),name='admin_create'),
]
