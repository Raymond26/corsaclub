# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Build, BuildMedia, Car, CarPurpose, FeaturedBuild, CarSubmission, BuildBulletPoint

admin.site.register(Build)
admin.site.register(BuildMedia)
admin.site.register(Car)
admin.site.register(CarPurpose)
admin.site.register(CarSubmission)
admin.site.register(FeaturedBuild)
admin.site.register(BuildBulletPoint)