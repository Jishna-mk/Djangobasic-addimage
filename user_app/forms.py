from django.forms import ModelForm
from dataclasses import fields
from.models import Productlist
# from dataclasses import fields


class ProductlistForm(ModelForm):
    class Meta:
        model = Productlist
        fields = "__all__"