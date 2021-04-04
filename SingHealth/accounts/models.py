from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField
from django.core.validators import MaxValueValidator,MinValueValidator
from multiselectfield import MultiSelectField
import datetime

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
    #status = models.ForeignKey(checklist,on_delete = models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, blank=True)
    category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, blank=True)
    actual_img = models.ImageField(upload_to ='images/')
    #score = models.FloatField(null=True)
    #checklist = models.ForeignKey(checklist,null=True,on_delete=models.SET_NULL)

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
    #actual_img = models.ImageField(upload_to = 'media/')
    #upload_file = models.ImageField(null=True,blank=True)

class tenant_score(models.Model):
    #some dummy model to work with the graph , the checklist model should be here instead  
    name=models.CharField(max_length=50)
    score=models.IntegerField()
    
    def __str__(self):
        return"{}-{}".format(self.name,self.score)

class Image(models.Model):
    #image_name = models.CharField(max_length=200)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.SET_NULL)
    actual_img = models.ImageField(upload_to ='images/')

    """ def __str__(self):
        return self.actual_img """

#class checklistconditions(models.Model):
    #description = models.CharField(max_length=20,null=True,default="null")
    #box = models.BooleanField(blank=True,default=False)
    
    #def __str__(self):
        #return self.description
    #this model contains the checklist conditions which can be added later on


class checklist(models.Model):
    VIOLATION = (
        ('Wet Floors','Wet Floors'),
        ('Oily floors','Oily floors'),
        ('Rats','Rats'),
        ('Safety Hazards','Safety Hazards'),
    )
    STATUS = (
    ('PASS','PASS'),
    ('FAIL','FAIL'),
    )
    tenant = models.ForeignKey(Tenant,null=True, on_delete = models.CASCADE, related_name='tenantchecklistscore')
    #items=models.ManyToManyField(checklistconditions,related_name="checklist")
    Staff=models.ForeignKey(User,null=True, on_delete = models.CASCADE, related_name='staffscore')
    score = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(10),MinValueValidator(1)])##input score for tenant
    status = models.CharField(max_length=20,choices=STATUS,default=True)
    checklist_items = MultiSelectField(choices=VIOLATION,default=True,null=True,blank=True)
    date_audited = models.DateTimeField(default=datetime.datetime.now)
    #actual_img = models.ImageField()
  
    def __str__(self):
        return self.tenant.name + " has scored " + str(self.score)

    


    




