from django.db import models

# Create your models here.
class DataProfile (models.Model):
    name = models.CharField(max_length=250)
    birthday = models.CharField(max_length=20)
    gender = models.CharField(max_length=200)
    expertise = models.CharField(max_length=250)
    email = models.CharField(max_length=200)
    description = models.CharField(max_length=250)