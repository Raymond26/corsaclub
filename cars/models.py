# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cardb.helpers import django_enum
from enum import Enum, unique
from django_extensions.db.fields import AutoSlugField
from tuners.models import Tuner
import markdown2

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    generation = models.CharField(max_length=100, null=True, blank=True)
    slug = AutoSlugField('slug', max_length=100, unique=True, populate_from=('make', 'model', 'generation','trim'), blank=False, null=False)
    trim = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        base = "%s %s" % (self.make, self.model)
        if self.generation is not None:
            base += " %s" % self.generation
        if self.trim is not None:
            base += " %s" % self.trim
        return base


class CarPurpose(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color_hex = models.CharField(max_length=6, unique=True)
    slug = AutoSlugField('slug', max_length=100, populate_from=('name'), blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Build(models.Model):
    name = models.CharField(max_length=200)
    add_timestamp = models.DateTimeField()
    preview_image = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    car = models.ForeignKey(Car)
    slug = AutoSlugField('slug', max_length=100, unique=True, populate_from=('name'), blank=False, null=False)
    tuners = models.ManyToManyField(Tuner, blank=True)
    purpose = models.ManyToManyField(CarPurpose)
    ig_handle = models.CharField(max_length=100, null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    youtube_channel = models.CharField(max_length=100, null=True, blank=True)
    build_thread = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    def build_media_preview(self):
        return self.buildmedia_set.all()[:3]

    def description_as_html(self):
        return markdown2.markdown(self.description)

    def bullet_points_ordered(self):
        return self.buildbulletpoint_set.order_by('order')

class BuildMedia(models.Model):
    @unique
    @django_enum
    class BuildMediaType(Enum):
        YOUTUBE_VIDEO = 'YT'
        INSTAGRAM_PHOTO = 'IP'
        INSTAGRAM_VIDEO = 'IV'

    builds = models.ManyToManyField(Build)
    media_type = models.CharField(max_length=2, choices=[(choice.value, choice.name) for choice in BuildMediaType])
    remote_url = models.URLField(null=True, blank=True)
    external_id = models.CharField(max_length=200, null=True, blank=True)
    preview_image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return "%s : %s : %s" % (self.builds.first().name, self.media_type, self.remote_url)

class FeaturedBuild(models.Model):
    build = models.OneToOneField(Build)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.build.name

class CarSubmission(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    ig_handle = models.CharField(max_length=100, null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    youtube_channel_link = models.URLField(null=True, blank=True)
    make_and_model = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    build_thread = models.URLField(null=True, blank=True)

    def __str__(self):
        str = ""
        if self.name is not None:
            str = self.name
        return str + " %s" % self.make_and_model

class BuildBulletPoint(models.Model):
    build = models.ForeignKey(Build)
    bullet_point = models.CharField(max_length=200, null=False, blank=False)
    order = models.SmallIntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return "%s : %s" % (self.build.name, self.bullet_point)