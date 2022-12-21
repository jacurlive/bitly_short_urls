from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from apps.models import Url, User


class UrlForm(forms.ModelForm):
    # long_name = forms.URLField(max_length=255)

    class Meta:
        model = Url
        exclude = ('short_name',)


class CustomLoginForm(AuthenticationForm):
    pass


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=PasswordInput(attrs={'autocomplete': 'current-password'}),)

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Check your password')
        return make_password(password)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
