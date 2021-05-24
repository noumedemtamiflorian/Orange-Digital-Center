from django import forms
from django.forms import widgets

from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'category',
                  'image', 'quantity', 'price']
        widgets = {
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'quantity': widgets.NumberInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'min': "12"}),
            'category': widgets.Select(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'slug']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'slug': widgets.TextInput(attrs={'class': 'form-control'}),
        }
