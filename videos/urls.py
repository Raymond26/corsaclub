from django.conf.urls import url

from . import views

app_name = 'videos'
urlpatterns = [
    url(r'^$', views.VideosIndexView.as_view(), name='index'),
]