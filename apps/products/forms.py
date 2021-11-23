from django.db import models
from django.forms import fields, widgets
from apps.products.models import Product,ProductImage
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['is_stock',]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        }

class ProductImageForm(forms.ModelForm):

    class Meta:
        model=ProductImage
        fields = ['image',]
        widgets = {
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }