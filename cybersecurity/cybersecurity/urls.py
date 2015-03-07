from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from ajax_select import urls as ajax_select_urls
from trainingPortal import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cybersecurity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/lookups/', include(ajax_select_urls)),
	url(r'^forum/', include('pybb.urls', namespace='pybb')),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^trainingPortal/', include('trainingPortal.urls')), #application
	url(r'^test/', include('quiz.urls')),
	url(r'^messages/', include('postman.urls')),
	url(r'^', include('cms.urls')),
	url(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
