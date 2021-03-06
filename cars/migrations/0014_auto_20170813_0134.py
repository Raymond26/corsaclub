# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 08:34
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_auto_20170813_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=100, populate_from=('make', 'model', 'generation', 'trim'), unique=True, verbose_name='slug'),
        ),
    ]
