from .models import Customer
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'vat_id', 'street', 'city', 'country']