from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Audit, Image


class AuditForm(ModelForm):
    class Meta:
        model = Audit
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = Image
        fields = ['actual_img'] 