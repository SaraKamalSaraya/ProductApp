from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    first_name= forms.CharField(label='First name',required=True)
    last_name= forms.CharField(label='Last name',required=True)
    email= forms.EmailField(label='Email',required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name","email", "username", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        if self.instance.username == username:
            return username  
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username Already Exists.")
        return username