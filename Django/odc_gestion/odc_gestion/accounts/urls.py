from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views
app_name = "accounts"
urlpatterns = [
    path('', views.index, name="home"),
    path('accounts/signup/', views.sign_up, name="signup"),
    path('accounts/logout/', views.logout_views, name="logout"),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name="password_reset"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name="password_reset_confirm"),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name="password_reset_complete"),
    path('accounts/password_change/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),
]

# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/reset/done/ [name='password_reset_complete']