from django.conf.urls import patterns, url
from trainingPortal import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^about', views.about, name='about'),
		url(r'^chapters', views.chapters, name='chapters'),
		url(r'^user/profile/(?P<username>[\w\-]+)/', views.profile, name='profile'),
		url(r'^chapter/(?P<chapter_title>[\w\-]+)/$', views.chapter, name='chapter'),
		url(r'^chapter/(?P<chapter_title>[\w\-]+)/(?P<section_title>[\w\-]+)/$', views.section, name='section'),
		url(r'^learningStyleCompletion', views.learningStyle, name='learningStyle'),
		url(r'^statistics', views.statistics, name='statistics'),
		url(r'^help', views.help, name='help'),
		)