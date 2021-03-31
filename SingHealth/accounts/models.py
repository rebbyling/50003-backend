from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tenant(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),

    )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS, blank=True)
    category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, blank=True)
    #score = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Audit(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),

    )
    date_audited = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    #score = models.FloatField(null=True)
    comment = models.TextField(blank=True)
    #upload_file = models.ImageField(null=True,blank=True)






class tenant_score(models.Model):
    #some dummy model to work with the graph , the checklist model should be here instead  
    name=models.CharField(max_length=50)
    score=models.IntegerField()
    
    def __str__(self):
        return"{}-{}".format(self.name,self.score)





class checklistconditions(models.Model):
    description = models.CharField(max_length=20,null=True,default="null")
    box = models.BooleanField(blank=True,default=False)
    
    def __str__(self):
        return self.description
    #this model contains the checklist conditions which can be added later on


class Checklist(models.Model):
    items=models.ManyToManyField(checklistconditions,related_name="checklist")
    def __str__(self):
        return self.category


class ChecklistScore(models.Model):
    date_created = models.DateTimeField(default=timezone.now, null=True)
    score = models.PositiveIntegerField(null = True)
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete = models.CASCADE, related_name='tenant_checklist')
    def __str__(self):
        return str(self.date_created)[:10] + "; Score: " + str(self.score) + " (" + str(self.tenant.username) + ")" 

    ##models.Cascade when reference object is deleted , also deletes the object that have references to it .
    ##need to add dropdownlist

    


    




