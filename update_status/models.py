from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class Pengguna(models.Model):
    kode_identitas = models.CharField('Kode Identitas', max_length=20, primary_key=True, )
    nama = models.CharField('Nama', max_length=200)
    created_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=7))
    updated_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=7))

class Status(models.Model):
    pengguna = models.ForeignKey(Pengguna)
    status = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=7))

    def as_dict(self):
        return {
            "status": self.status,
            "created_date": self.created_date,
        }
        
class Comment(models.Model):
	pengguna = models.ForeignKey(Status,on_delete=models.CASCADE)
	comment = models.CharField(max_length=1000)
	created_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=7))