# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20170813_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='tuners',
            field=models.ManyToManyField(to='tuners.Tuner'),
        ),
    ]
