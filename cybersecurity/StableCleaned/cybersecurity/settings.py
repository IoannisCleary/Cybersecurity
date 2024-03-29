"""
Django settings for cybersecurity project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&gi@ruv#a$zwfsa5_+(61@)z!w&t$t1_4oa*8(5gey#01rgn#k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
	'django.core.context_processors.debug',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
    # allauth specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'pybb.context_processors.processor',
)
ACCOUNT_EMAIL_REQUIRED = False

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	TEMPLATE_PATH,
)
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nicolemaniac@gmail.com'
EMAIL_HOST_PASSWORD = 'kibpfkdhmcqyckxv'
DEFAULT_FROM_EMAIL = 'nicolemaniac@gmail.com'
DEFAULT_TO_EMAIL = 'ioanniscleary@gmail.com'
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_DISABLE_USER_EMAILING = True
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
	'django.contrib.admin',
	'pagination',
	'ajax_select',
	'mailer',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'django.contrib.messages',  # to enable messages framework (see :ref:`Enable messages <enable-messages>`)
	#django-allauth
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	'allauth.socialaccount.providers.facebook',
	'djangocms_file',
	'djangocms_flash',
	'djangocms_picture',
	'djangocms_video',
	'djangocms_link',
	'djangocms_text_ckeditor',
	'cms',  # django CMS itself
	'mptt',  # utilities for implementing a tree
	'menus',  # helper for model independent hierarchical website navigation
	'sekizai',  # for javascript and css management
	'filer',
	'easy_thumbnails',
	'ckeditor',
	'tinymce',
	'django_wysiwyg',
	'pytz',
	'postman',
	'transmeta',
	#django-quiz
	'quiz',
	'multichoice',
	'true_false',
	'essay',
	'pybb',
	#training portal
	'trainingPortal',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.doc.XViewMiddleware',
	'django.middleware.common.CommonMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',
	'pagination.middleware.PaginationMiddleware',
	'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'cybersecurity.urls'

WSGI_APPLICATION = 'cybersecurity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

SITE_ID = 1
# http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Add_django-allauth

LOGIN_REDIRECT_URL = '/trainingPortal/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/trainingPortal/'
SOCIALACCOUNT_QUERY_EMAIL = True

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       { 'SCOPE': ['email'],
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False}}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

DJANGO_WYSIWYG_FLAVOR = "tinymce_advanced"
CKEDITOR_UPLOAD_PATH = "/media/uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
           'awesome_ckeditor': {
               'toolbar': 'full',
               'height': "auto",
               'width': "auto",
           },
           'default': {
               'toolbar': 'full',
               'height': "auto",
               'width': "auto",
           },
       }

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ACCOUNT_SIGNUP_FORM_CLASS =('trainingPortal.forms.RegisterForm')
SOCIALACCOUNT_FORMS = {'signup': 'trainingPortal.forms.RegisterForm'}
TINYMCE_JS_URL = os.path.join(STATIC_ROOT, "/tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "advlist autolink lists link image charmap print preview hr anchor pagebreak searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking save table contextmenu directionality emoticons template paste textcolor colorpicker textpattern",
    'theme': "advanced",
    'cleanup_on_startup': True,
     'toolbar1': "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
    'toolbar2': "print preview media | forecolor backcolor emoticons",
    'custom_undo_redo_levels': 15,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True

LANGUAGES = [
    ('en', 'English'),
]

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menus': 'menus.migrations_django',

    # Add also the following modules if you're using these plugins:
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_snippet': 'djangocms_snippet.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
}

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (65, 65), 'crop': 'smart'},
    },
}

PYBB_TOPIC_PAGE_SIZE = 10
PYBB_FORUM_PAGE_SIZE = 20
PYBB_USERS_PAGE_SIZE = 20
PYBB_AVATAR_WIDTH = 60
PYBB_AVATAR_HEIGHT = 60
PYBB_DEFAULT_TIME_ZONE = 3
PYBB_SIGNATURE_MAX_LENGTH = 1024
PYBB_SIGNATURE_MAX_LINES = 3
PYBB_QUICK_TOPICS_NUMBER = 10
PYBB_QUICK_POSTS_NUMBER = 10
PYBB_READ_TIMEOUT = 3600 * 24 * 7 # seconds
#PYBB_POST_AUTOJOIN_ENABLED = True
#PYBB_POST_AUTOJOIN_TIMEOUT = 60 * 60 # seconds
PYBB_DEFAULT_MARKUP = 'bbcode'
PYBB_FREEZE_FIRST_POST = True
PYBB_ADMIN_URL = '/admin/'
PYBB_ATTACHMENT_SIZE_LIMIT = 1024 * 1024
PYBB_ATTACHMENT_ENABLE = True
PYBB_SKIN = 'default'

PYBB_ATTACHMENT_UPLOAD_TO = os.path.join('pybb_upload', 'attachments')
PYBB_DEFAULT_AVATAR_URL = 'pybb/img/anonymous.gif'
PYBB_REBUILD_PRIMARY_PERIOD = 600