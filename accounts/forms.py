from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Електронна пошта", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': "Ім'я користувача",
        }
        help_texts = {
            'username': '',
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="Електронна пошта", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': "Ім'я користувача",
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': "Аватарка",
        }