# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halaman_profile', '0002_auto_20171212_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.CharField(max_length=20)),
                ('level', models.CharField(choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced'), ('4', 'Expert')], default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('npm', models.CharField(max_length=20, unique=True)),
                ('profile_pic', models.URLField(default='https://www.lausanne.org/wp-content/uploads/2017/04/anonymous-icon-150x150.jpg')),
                ('flag_nilai', models.BooleanField(default=False)),
                ('name', models.CharField(default='Kosong', max_length=27)),
                ('email', models.EmailField(default='Kosong', max_length=254)),
                ('linkedin_profile', models.URLField(default='Kosong')),
                ('expertise', models.ManyToManyField(default='Kosong', to='halaman_profile.Expertise')),
            ],
        ),
        migrations.DeleteModel(
            name='DataProfile',
        ),
    ]