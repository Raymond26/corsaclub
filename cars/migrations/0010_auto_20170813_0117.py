# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20170810_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildmedia',
            name='build',
        ),
        migrations.AddField(
            model_name='buildmedia',
            name='builds',
            field=models.ManyToManyField(to='cars.Build'),
        ),
        migrations.AlterField(
            model_name='buildmedia',
            name='media_type',
            field=models.CharField(choices=[('YT', 'YOUTUBE_VIDEO'), ('IP', 'INSTAGRAM_PHOTO'), ('IV', 'INSTAGRAM_VIDEO')], max_length=2),
        ),
    ]
