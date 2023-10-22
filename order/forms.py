from django import forms
from .models import Order, ProductOrder


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'status',]


class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity']
