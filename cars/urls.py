from django.conf.urls import url

from . import views

app_name = 'cars'
urlpatterns = [
  #url(r'^$', views.cars_index, name='index'),
  #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^$', views.featured_builds, name='featured_builds'),
  url(r'^builds/ig_media$', views.get_instagram_media, name='get_instagram_media'),
  url(r'^about$', views.about, name='about'),
  url(r'^contact$', views.contact, name='contact'),
  url(r'^submit$', views.submit, name='submit'),
  url(r'^submit/success$', views.submit_success, name='submit_success'),
  url(r'^browse', views.browse, name='browse'),
  url(r'^category/(?P<slug>[\w-]+)/$', views.cars_by_purpose, name='cars_by_purpose'),
  url(r'^cars/(?P<slug>[\w-]+)/$', views.car_view, name='car_detail'),
  url(r'^(?P<slug>[\w-]+)/$', views.build_view, name='build_view'),
  url(r'^(?P<slug>[\w-]+)/feedback/$', views.send_build_feedback, name='send_build_feedback'),
  url(r'^(?P<slug>[\w-]+)/add_media/$', views.add_build_media, name='add_build_media'),
]
