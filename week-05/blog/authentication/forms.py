from django.forms import ModelForm
from django import forms
from .models import User


class RegisterForm(ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password_again = forms.CharField(max_length=255, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email']

    def is_valid(self):
        valid = super().is_valid()
        if self.data.get('password_again') != self.data.get('password'):
            self.add_error('', 'Passwords mismatch')
            return False
        return valid


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

