# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views import generic

from .models import Video

class VideosIndexView(generic.ListView):
    template_name = 'videos/index.html'
    context_object_name = 'videos_list'

    def get_queryset(self):
        return Video.objects.order_by('add_timestamp')[:20]