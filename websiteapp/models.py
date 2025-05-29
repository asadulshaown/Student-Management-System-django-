from django.db import models

# Create your models here.
class Members(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  roll = models.CharField(max_length=50)
  password = models.CharField(max_length=16)