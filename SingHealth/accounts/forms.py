from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Audit


class AuditForm(ModelForm):
    class Meta:
        model = Audit
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class checklistForm(forms.Form): 
    health1 = forms.BooleanField(required = False)
    health2 = forms.BooleanField(required = False)
    health3 = forms.BooleanField(required = False)
    safety1 = forms.BooleanField(required = False)
    safety2 = forms.BooleanField(required = False)

    
    
