# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataprofile',
            name='linkedin',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataprofile',
            name='npm',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
