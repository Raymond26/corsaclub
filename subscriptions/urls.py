from django.conf.urls import url

from . import views

app_name = 'subscriptions'
urlpatterns = [
    url(r'^$', views.subscription_signup, name='subscription_signup'),
]