# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-11 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('update_status', '0002_auto_20171211_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 22, 30, 24, 323148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 22, 30, 24, 322145, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pengguna',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 22, 30, 24, 322145, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 22, 30, 24, 322676, tzinfo=utc)),
        ),
    ]
