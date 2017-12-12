
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class User(models.Model):
    kode_identitas = models.CharField('Kode Identitas', max_length=20, primary_key=True, default='Kosong')
    firstName = models.CharField('Nama Depan', max_length=225)
    lastName = models.CharField('Nama Belakang', max_length=225)
    imageUrl = models.URLField('Foto')
    email = models.EmailField('Email', default='Kosong')
    profileUrl = models.URLField('Profile LinkedIn', default='Kosong')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Expertise(models.Model):
    user = models.ForeignKey(User)
    expert = models.CharField('Keahlian', max_length=27)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
