from django.db import models
import datetime 

# Create your models here.
class tenant(models.Model):
    Tenant_Shop = models.CharField(max_length=30,default=None)
    Auditor = models.CharField(max_length=30,default=None)
    date = models.DateField(("Date"), default=datetime.date.today)
    done =models.BooleanField(default=False)
    
    def __str__(self):
        return self.Tenant_Shop
