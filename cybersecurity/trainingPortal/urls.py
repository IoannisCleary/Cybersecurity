from django.conf.urls import patterns, url
from trainingPortal import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
		url(r'^chapters', views.chapters, name='chapters'),
		url(r'^user/profile/(?P<username>[\w\-]+)/', views.profile, name='profile'),
		url(r'^chapter/(?P<chapter_title>[\w\-]+)/$', views.chapter, name='chapter'),
		url(r'^chapter/(?P<chapter_title>[\w\-]+)/(?P<page_title>[\w\-]+)/$', views.page, name='page'),
		
		)