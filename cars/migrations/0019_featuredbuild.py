# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_auto_20170818_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.SmallIntegerField()),
                ('build', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.Build')),
            ],
        ),
    ]
