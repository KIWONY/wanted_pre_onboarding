from django.db import models

# Create your models here.
from Company.models import Companys

# User가 접근할 수 있는 목록
class JobOpen(models.Model):
    company = models.ForeignKey('Company.Companys', on_delete=models.CASCADE, null = True, related_name="company")
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    position = models.CharField(max_length=500, null=False)
    compensation = models.IntegerField(null=False)
    description = models.TextField(null=False)
    skills = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.company

