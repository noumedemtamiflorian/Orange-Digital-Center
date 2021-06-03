from django.contrib import admin
from django.urls import path
from . import views

app_name = "fournisseur"
urlpatterns = [
    path('fournisseurs/', views.index, name="index"),
    path('fournisseur/<int:id>', views.detail, name="detail"),
    path('fournisseur/new', views.new, name="new"),
    path('fournisseur/<int:id>/edit', views.edit, name="edit"),
    path('fournisseur/<int:id>/delete', views.delete, name="delete"),
]
