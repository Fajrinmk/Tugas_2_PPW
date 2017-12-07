from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pengguna(models.Model):
    kode_identitas = models.CharField('Kode Identitas', max_length=20, primary_key=True, )
    nama = models.CharField('Nama', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class myStatus(models.Model):
    pengguna = models.ForeignKey(Pengguna)
    status = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)

class myComment(models.Model):
	pengguna = models.ForeignKey(myStatus)
	comment = models.CharField(max_length=1000)
	updated_at = models.DateTimeField(auto_now=True)