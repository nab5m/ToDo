from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import UserProfile


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password1', 'password2', 'address', 'phone', 'birth_date']


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
