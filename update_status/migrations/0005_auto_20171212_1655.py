# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 09:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0004_merge_20171212_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 16, 55, 23, 768484, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 16, 55, 23, 767482, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 16, 55, 23, 767983, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 16, 55, 23, 767983, tzinfo=utc)),
        ),
    ]
