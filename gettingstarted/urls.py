from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hoosin.views

urlpatterns = patterns('',
    url(r'^$', hoosin.views.default, name='index'),
    url(r'^new_hours_submit', hoosin.views.new_hours_submission_hook, name='new_hours')
)
