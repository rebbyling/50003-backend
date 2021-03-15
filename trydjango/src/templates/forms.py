from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms #django default user model
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
        widgets = {
            'myfield' : forms.textInput(attrs={'class': 'searchBar'}),
        }