# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-13 00:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0026_merge_20171213_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 7, 0, 28, 168038, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 7, 0, 28, 166533, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 7, 0, 28, 166533, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 13, 7, 0, 28, 167536, tzinfo=utc)),
        ),
    ]
