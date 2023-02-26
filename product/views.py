from urllib import request
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ProductForms


class CreateProductView(CreateView):
    form_class = ProductForms
    template_name = 'product/admin_create.html'
    success_url='/home/' #change to be

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()        
        kwargs['user'] = self.request.user
        return kwargs


