# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tuners.models import Tuner
from cars.models import Car

class Video(models.Model):
    remote_url = models.CharField(max_length=300)
    add_timestamp = models.DateTimeField()
    youtube_id = models.CharField(max_length=100, null=True)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    tuner = models.ForeignKey(Tuner, blank=True, null=True)

    def __str__(self):
        base = '%s' % self.car
        base += ' %s' % self.youtube_id
        return base