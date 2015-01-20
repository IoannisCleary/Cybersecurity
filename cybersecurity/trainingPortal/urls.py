from django.conf.urls import patterns, url
from trainingPortal import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
		url(r'^chapter/(?P<category_title>[\w\-]+)/$', views.chapter, name='chapter'),)