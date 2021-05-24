from django.contrib.auth import forms, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm
)
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm


@login_required
def index(request):
    return render(request, 'accounts/index.html')


def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'accounts/index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)


def logout_views(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, 'registration/logout.html')
