from dataclasses import field
from django.forms import ModelForm
from .models import Product
from accounts.models import CustomUser

class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = [
            "customuser",
            "name",
            "description",
            "price",
            "image",
            "stock"
        ]


    def __init__(self, user, *args, **kwargs):
        super(ProductForms, self).__init__(*args, **kwargs)
        self.fields['customuser'].empty_label = None

        self.fields['customuser'].queryset = CustomUser.objects.filter(username=user.username)


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "image",
            "stock"
        ]
