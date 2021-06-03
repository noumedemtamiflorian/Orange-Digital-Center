from django.contrib import admin
from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path('products/', views.index, name="index"),
    path('product/<int:id>', views.detail, name="detail"),
    path('products/<slug:slug>', views.productByCategory, name="product_category"),
    path('product/new', views.new, name="new"),
    path('product/<int:id>/edit', views.edit, name="edit"),
    path('product/<int:id>/delete', views.delete, name="delete"),

    path('categories/', views.index_category, name="categories"),
    path('products/<slug:slug>', views.productByCategory, name="product_category"),
    path('category/new', views.new_category, name="new_category"),
    path('category/<int:id>/edit', views.edit_category, name="edit_category"),
    path('category/<int:id>/delele',
         views.delete_category, name="delete_category"),
]
