"""
Django settings for cybersecurity project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&gi@ruv#a$zwfsa5_+(61@)z!w&t$t1_4oa*8(5gey#01rgn#k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
	# Required by allauth template tags
    "django.core.context_processors.request",
	'django.contrib.auth.context_processors.auth',
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
	'trainingPortal',
	#django-allauth
	'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.amazon',
    'allauth.socialaccount.providers.angellist',
    'allauth.socialaccount.providers.bitbucket',
    'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.coinbase',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.feedly',
    'allauth.socialaccount.providers.fxa',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.linkedin_oauth2',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.soundcloud',
    'allauth.socialaccount.providers.stackexchange',
    'allauth.socialaccount.providers.tumblr',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.vimeo',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.xing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'SCOPE': ['email', 'publish_stream'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.2'}}