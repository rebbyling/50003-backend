from django.forms import ModelForm , Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Audit, Image, Tenant
from django import forms
from .models import checklist
from django.utils.translation import gettext_lazy as _

#class AddItemForm(forms.ModelForm):
    #class Meta:
       # model = checklistconditions
        #fields = [
         #   'description',
        #]
        
#class CheckboxForm(forms.ModelForm):
   #class Meta:
       # model = checklist
        #fields = ['items']
        
    #items = forms.ModelMultipleChoiceField(queryset = checklistconditions.objects.all(),widget = forms.CheckboxSelectMultiple ,label = "")
    #overwriting the

class ScoreForm(forms.ModelForm):
    class Meta:
        model = checklist
        fields = ['tenant','checklist_items','score','status','comment']
        widgets = {
          'comment': Textarea(attrs={'rows':3, 'cols':10}),
        }
        
    
    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)##model forms init method is being called
        #self.fields['items'] = forms.ModelMultipleChoiceField(
               # queryset = checklist.objects.all(),##get all the attributes of the model which are items ,items model link to checklist conditions
               # widget = forms.CheckboxSelectMultiple,
               #label = "",
            #)       
class AuditForm(ModelForm):
    class Meta:
        model = checklist
        fields = ['tenant', 'checklist_items', 'score']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = Image
        fields = ['tenant','actual_img']