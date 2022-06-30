from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Highlight, Profile


class HighlightForm(ModelForm):
    class Meta:
        model = Highlight
        fields = '__all__'
        exclude = ('user',)
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'profile_pic')
  
# Crear formulario de de registro de usuarios personalizado
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        