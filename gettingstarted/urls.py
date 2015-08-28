from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hoosin.views

urlpatterns = patterns('',
    url(r'^$', hoosin.views.default, name='index'),
)
