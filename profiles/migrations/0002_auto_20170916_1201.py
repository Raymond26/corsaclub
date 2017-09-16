# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0025_auto_20170916_1041'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('8270cbba-6238-487e-8245-7c81a02998eb'), primary_key=True, serialize=False)),
                ('start_timestamp', models.DateTimeField(auto_now_add=True)),
                ('latest_request_timestamp', models.DateTimeField(auto_now_add=True)),
                ('platform', models.CharField(choices=[('1', 'WEB'), ('2', 'IOS'), ('3', 'ANDROID'), ('0', 'OTHER')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserBuildImpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Build')),
            ],
        ),
        migrations.CreateModel(
            name='UserBuildView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Build')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_seen_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_seen_timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='session_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='userbuildview',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
        migrations.AddField(
            model_name='userbuildimpression',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
        migrations.AddField(
            model_name='session',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
        migrations.AddField(
            model_name='pageview',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Session'),
        ),
        migrations.AddField(
            model_name='pageview',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile'),
        ),
    ]
