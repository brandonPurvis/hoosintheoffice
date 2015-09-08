from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hoosin.views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hoosin.views.default, name='index'),
    url(r'^new_hours_form', hoosin.views.go_to_office_hours_form),
    url(r'^new_hours_submit', hoosin.views.new_hours_submission_hook, name='new_hours'),
    url(r'^search', hoosin.views.search_hook, name='search'),
)
