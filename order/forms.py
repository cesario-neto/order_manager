from django import forms
from .models import Order, ProductOrder


class OrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'status',]
        widgets = {
            'client': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select form-select-sm',
            })
        }


class ProductForms(forms.ModelForm):
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-select form-select-sm',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',

            }),
        }
