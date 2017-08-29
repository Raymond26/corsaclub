# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_car_trim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='build',
            name='preview_image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
