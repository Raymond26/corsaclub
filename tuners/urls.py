from django.conf.urls import url

from . import views

app_name = 'tuners'
urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.tuner_view, name='tuner_view'),
    url(r'^$', views.tuner_list, name ='tuner_list')
]