# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_extensions.db.fields import AutoSlugField

class Tuner(models.Model):
    name = models.CharField(max_length=200)

    slug = AutoSlugField('slug', max_length=100, unique=True, populate_from=('name',), blank=False, null=False)

    def __str__(self):
        return self.name