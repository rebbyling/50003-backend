from django import forms 
from .models import *

class healthForm(forms.ModelForm): 
  
    class Meta: 
        model = healthForm
        fields = ['requirements']