from django import forms
from django.forms import widgets
from .models import Produits


class addProduitForm(forms.ModelForm):

    class Meta:
        model = Produits
        fields = [
            'nom',
            'prix',
            'marque',
            'code',
            'category',
            'image'
        ]
    widgets = {
            'nom': widgets.TextInput(attrs={"class":"form-control"}),
            'prix': widgets.NumberInput(attrs={"class":"form-control"}),
            'marque': widgets.TextInput(attrs={"class":"form-control"}),
            'code': widgets.TextInput(attrs={"class":"form-control"}),
            'categorie': widgets.Select(attrs={"class": "form-control"}),
        }