from django.db import models


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




class tenant_score(models.Model):
    #some dummy model to work with the graph , the checklist model should be here instead  
    name=models.CharField(max_length=50)
    score=models.IntegerField()
    
    def __str__(self):
        return"{}-{}".format(self.name,self.score)
         





