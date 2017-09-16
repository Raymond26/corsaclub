# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.contrib.admin.views.decorators import staff_member_required

from .models import Build, Car, BuildMedia, FeaturedBuild, CarSubmission, CarPurpose
from tuners.models import Tuner
from videos.models import Video
from videos.services import instagram_embed_retrieve, youtube_embed_retrieve

import markdown2
import requests

def cars_index(request):
    cars = Car.objects.order_by('make')
    template = loader.get_template('cars/index.html')
    context = {
        'cars' : cars
    }
    return HttpResponse(template.render(context, request))


class DetailView(generic.DetailView):
    model = Build
    template_name = 'cars/detail.html'


def car_view(request, slug):
    car = Car.objects.filter(slug=slug)[0]
    builds = Build.objects.filter(car=car)

    template = loader.get_template('cars/car_detail.html')
    context = {
        'car' : car,
        'builds' : builds,
        'build_media_types' : BuildMedia.BuildMediaType
    }
    return HttpResponse(template.render(context, request))


def build_view(request, slug):
    build = Build.objects.filter(slug=slug)[0]
    build_media = BuildMedia.objects.filter(builds=build)
    build_description_as_html = markdown2.markdown(build.description)

    template = loader.get_template('cars/build_view.html')
    context = {
        'build' : build,
        'build_media' : build_media,
        'build_media_types' : BuildMedia.BuildMediaType
    }
    return HttpResponse(template.render(context, request))

@staff_member_required
def add_build_media(request, slug):
    build_arr = Build.objects.filter(slug=slug)
    if len(build_arr) == 0:
        return HttpResponseNotFound("build not found")

    build = build_arr[0]
    if request.method == 'GET':
        template = loader.get_template('cars/add_build_media.html')
        context = {
            'build' : build,
            'build_media_types' : BuildMedia.BuildMediaType
        }

        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        media_type_raw = request.POST['media-type-input']
        media_type = BuildMedia.BuildMediaType[media_type_raw]
        external_id = request.POST['external-id-input']

        if media_type == BuildMedia.BuildMediaType.YOUTUBE_VIDEO:
            build_media = youtube_embed_retrieve(external_id)
            build_media.save()
            build_media.builds=[build]
            build_media.save()
        elif media_type == BuildMedia.BuildMediaType.INSTAGRAM_PHOTO or media_type == BuildMedia.BuildMediaType.INSTAGRAM_VIDEO:
            build_media = instagram_embed_retrieve(external_id, media_type)
            build_media.save()
            build_media.builds=[build]
            build_media.save()
        else:
            return HttpResponseRedirect('/')



    return HttpResponseRedirect('/')

def get_instagram_media(request):
    ig_url = request.GET["url"]
    api_response = requests.get("https://api.instagram.com/oembed?url=" + ig_url)
    return HttpResponse(api_response.text, content_type="application/json")


def featured_builds(request):
    template = loader.get_template('cars/featured_builds.html')
    featured = FeaturedBuild.objects.order_by('order')
    builds = []
    for fb in featured:
        builds.append(fb.build)
    context = {
        'builds' : builds,
        'build_media_types' : BuildMedia.BuildMediaType
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('cars/about.html')
    return HttpResponse(template.render(None, request))


def contact(request):
    template = loader.get_template('cars/contact.html')
    return HttpResponse(template.render(None, request))


def submit(request):
    if request.method == 'GET':
        template = loader.get_template('cars/submit.html')
        return HttpResponse(template.render(None, request))
    elif request.method == 'POST':
        name = request.POST['name-input']
        description = request.POST['description-input']
        ig_handle = request.POST['ig-handle-input']
        twitter_handle = request.POST['twitter-handle-input']
        yt_channel = request.POST['youtube-channel-input']
        make_model = request.POST['make-model-input']
        build_thread = request.POST['build-thread-input']
        submission = CarSubmission(
            name=name,
            ig_handle=ig_handle,
            twitter_handle=twitter_handle,
            youtube_channel_link=yt_channel,
            make_and_model=make_model,
            description=description,
            build_thread=build_thread
        )
        submission.save()
        return HttpResponseRedirect("/submit/success")


def submit_success(request):
    template = loader.get_template('cars/submit_success.html')
    return HttpResponse(template.render(None, request))


def browse(request):
    template = loader.get_template('cars/browse.html')
    context = {
        'tuners' : Tuner.objects.all(),
        'cars' : Car.objects.order_by('make'),
        'purposes' : CarPurpose.objects.all()
    }
    return HttpResponse(template.render(context, request))


def cars_by_purpose(request, slug):
    purpose = CarPurpose.objects.filter(slug=slug)[0]
    builds = purpose.build_set.all()
    template = loader.get_template('cars/builds_by_purpose.html')
    context = {
        'purpose' : purpose,
        'builds' : builds,
        'build_media_types' : BuildMedia.BuildMediaType
    }
    return HttpResponse(template.render(context, request))