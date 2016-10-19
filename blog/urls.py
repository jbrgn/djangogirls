from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.thing_list, name='thing_list'),
    url(r'^things/(\d+)/$', views.thing_detail, name='thing_detail'),
    url(r'^about/$', views.about, name='about'),
]
