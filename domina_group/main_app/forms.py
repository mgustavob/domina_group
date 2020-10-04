from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class profileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

# class Meta(UserCreationForm.Meta):
#     model = User
#     fields = UserCreationForm.Meta.fields + ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2' )
