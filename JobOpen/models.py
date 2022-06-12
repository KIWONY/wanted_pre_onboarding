from django.db import models

# Create your models here.

class JobOpen(models.Model):
    company = models.CharField(max_length=500,null=False)
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    position = models.CharField(max_length=500, null=False)
    compensation = models.IntegerField(null=False)
    description = models.TextField(null=False)
    skills = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.company