# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('signup_timestamp', models.DateTimeField(auto_now_add=True)),
                ('unsubscribed', models.BooleanField(default=False)),
            ],
        ),
    ]
