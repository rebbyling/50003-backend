from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    comments = models.TextField()
    status = models.CharField(max_length=30, blank=True)
    submission_date = models.DateTimeField()

    def __str__(self):
        return self.name
