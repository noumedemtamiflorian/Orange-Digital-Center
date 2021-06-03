from django import forms
from django.forms import widgets

from .models import Fournisseur


class FournisseurForm(forms.ModelForm):
    
    class Meta:
        model = Fournisseur
        fields = ['name', 'email', 'number', 'addresse']
