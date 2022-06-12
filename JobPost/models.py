from django.db import models

# Create your models here.
class JobPost(models.Model):
    position = models.CharField(max_length=500, null=False)
    compensation = models.IntegerField(null=False)
    description = models.TextField(null=False)
    skills = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.position