# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 10:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0008_auto_20171212_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 17, 55, 25, 739206, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 17, 55, 25, 736699, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 17, 55, 25, 736699, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 17, 55, 25, 737702, tzinfo=utc)),
        ),
    ]
