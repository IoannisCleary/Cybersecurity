from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cybersecurity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('allauth.urls')),
	url(r'^trainingPortal/', include('trainingPortal.urls')), #application
	url(r'^messages/', include('postman.urls')),
	url(r'^', include('cms.urls')),
	url(r'^ckeditor/', include('ckeditor.urls')),
	url(r'^tinymce/', include('tinymce.urls')),		
	# questionnaire urls
    url(r'q/', include('questionnaire.urls')),
    url(r'^take/(?P<questionnaire_id>[0-9]+)/$', 'questionnaire.views.generate_run'),
    url(r'^$', 'questionnaire.page.views.page', {'page_to_render' : 'index'}),
    url(r'^(?P<lang>..)/(?P<page_to_trans>.*)\.html$', 'questionnaire.page.views.langpage'),
    url(r'^(?P<page_to_render>.*)\.html$', 'questionnaire.page.views.page'),
    url(r'^setlang/$', 'questionnaire.views.set_language'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
