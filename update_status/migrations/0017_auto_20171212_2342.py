# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 16:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0016_auto_20171212_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 23, 42, 33, 930611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 23, 42, 33, 929149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 23, 42, 33, 929149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 23, 42, 33, 929648, tzinfo=utc)),
        ),
    ]