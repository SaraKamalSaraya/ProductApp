from django.shortcuts import render,redirect,reverse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView , DeleteView, UpdateView
from django.contrib.auth.models import  User
from accounts.forms import  RegisterForm
from django.urls import reverse_lazy

# Create your views here.

class Profile(DetailView):
    model= User
    template_name = 'registration/profile.html'
    def get_object(self, queryset=None):
      return self.request.user #return the currently logged-in user.

class Register(CreateView):
    model: User
    template_name = 'registration/registeration.html'
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    
class Edit_Profile(UpdateView):
    model= User
    template_name = 'registration/edit_profile.html'
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    def get_object(self, queryset=None):
        return self.request.user #return the currently logged-in user.

class Delete_Profile(DeleteView):
    model= User
    template_name = 'registration/delete_profile.html'
    success_url = reverse_lazy("accounts.Register")
    def get_object(self, queryset=None):
        return self.request.user #return the currently logged-in user.