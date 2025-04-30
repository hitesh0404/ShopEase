from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email','user_type']