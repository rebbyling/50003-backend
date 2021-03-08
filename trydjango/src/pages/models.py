from django.db import models

# Create your models here.
class tenants(models.Model):
    shop_name = models.CharField(max_length=20,null=True)
    auditor = models.CharField(max_length=20,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    done= models.BooleanField(None)

    def __str__ (self):
        return self.shop_name

