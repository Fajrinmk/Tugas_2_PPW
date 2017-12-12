from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
	nama = models.CharField(max_length=400)
	npm = models.CharField(max_length=250)
	angkatan = models.CharField(max_length=400)
	keahlian = models.CharField(max_length=400)