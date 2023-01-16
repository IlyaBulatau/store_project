from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class ProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=250, help_text='user@gmail.com')
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']