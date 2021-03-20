from django.db import models
from django import forms

# Create your models here.
class healthForm(forms.Form):
    health1 = forms.BooleanField(required = False)
    health2 = forms.BooleanField(required = False)
    health3 = forms.BooleanField(required = False)
#    testing = forms.BooleanField()
#    halo_world = forms.BooleanField()

class safetyForm(forms.Form):
    safety1 = forms.BooleanField(required = False)
    safety2 = forms.BooleanField(required = False)