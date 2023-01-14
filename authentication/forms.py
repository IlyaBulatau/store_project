from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=250, help_text='user@gmail.com')

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email','password1', 'password2')
