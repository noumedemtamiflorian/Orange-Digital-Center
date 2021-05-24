from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class LoginForm(AuthenticationForm):

    username = forms.CharField(required=True
        ,max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password',)
