# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from videos.models import Video

from cars.models import BuildMedia
from .models import Tuner

def tuner_view(request, slug):
    tuner = Tuner.objects.filter(slug=slug)[0]

    template = loader.get_template('tuners/detail.html')
    context = {
        'tuner' : tuner,
        'build_media_types' : BuildMedia.BuildMediaType
    }
    return HttpResponse(template.render(context, request))

def tuner_list(request):
    tuners = Tuner.objects.order_by('name')[:50]

    template = loader.get_template('tuners/index.html')
    context = {
        'tuners' : tuners
    }
    return HttpResponse(template.render(context, request))