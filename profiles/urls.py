from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    url(r'^sync/$', views.sync_customer_product_user, name='sync_customer_product_user')
]