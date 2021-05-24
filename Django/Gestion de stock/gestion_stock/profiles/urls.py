from django.contrib import admin
from django.urls import path
from . import views
app_name = "profiles"
urlpatterns = [
    path('<str:username>', views.detail, name="profiles"),
]
