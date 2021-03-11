from django.db import models

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length=200)
    actual_img = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.actual_img