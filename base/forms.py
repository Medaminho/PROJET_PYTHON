from django import forms
from .models import Order,Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client_name', 'address', 'telephone', 'email', 'product', 'qte', 'status']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'qte', 'prix']
