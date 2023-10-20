

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from accounts.views import Profile,Register,Edit_Profile,Delete_Profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('accounts/profile/', login_required(Profile.as_view()) ,name='profile'),
    path('logout/', LogoutView.as_view(template_name='accounts/login.html'), name='logout'),
    path('register/', Register.as_view(), name='accounts.Register'),
    path('edit-profile/', Edit_Profile.as_view(), name='accounts.edit_profile'),
    path('delete-profile/', Delete_Profile.as_view(), name='accounts.delete_profile'),
]