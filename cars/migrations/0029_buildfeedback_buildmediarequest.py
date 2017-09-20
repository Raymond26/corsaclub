# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0028_buildmedia_add_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_feedback', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Build')),
            ],
        ),
        migrations.CreateModel(
            name='BuildMediaRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('YT', 'YOUTUBE_VIDEO'), ('IP', 'INSTAGRAM_PHOTO'), ('IV', 'INSTAGRAM_VIDEO')], max_length=2)),
                ('remote_url', models.URLField()),
                ('external_id', models.CharField(max_length=200)),
                ('request_timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Build')),
            ],
        ),
    ]
