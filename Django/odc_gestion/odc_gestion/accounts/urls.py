from django.contrib import admin
from django.urls import path
from . import views
app_name = "accounts"
urlpatterns = [
    path('', views.index, name="home"),
    path('accounts/signup/', views.sign_up, name="signup"),
    path('accounts/logout/', views.logout_views, name="logout"),
]
