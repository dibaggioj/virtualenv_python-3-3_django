"""
Django settings for mysite project.

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
SECRET_KEY = '9bh7@0zuwi55!nf&__mi*swxcdl+cr$&au=vv(0i4tj4dz)pnq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'polls',
    'photos',
    'mysite',
    # 'debug_toolbar',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
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

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # stores db.sqlite3 in the project (base) directory
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mysite_django_storage',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         # 'HOST': '127.0.0.1',
#         'HOST': 'localhost',
#         # 'HOST': '/var/run/mysql',
#         'PORT': '3306',
#     }
# }
# some other database options:
# 'django.db.backends.postgresql_psycopg2', 
# 'django.db.backends.mysql', 
# 'django.db.backends.oracle',
# and see https://docs.djangoproject.com/en/1.7/ref/databases/#third-party-notes

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

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))

MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '971893029491183'
SOCIAL_AUTH_FACEBOOK_SECRET = 'dca8b103143268e2c77f350676411f94'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '456216769390-l9vu8l3qt4rdlhboormicbpfl0mlbgob.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'aUzdi9Ee-fEkm2bZTbnueMWp'

SOCIAL_AUTH_TWITTER_KEY = 'gx2xgivu40KRedMqLis8R5FSA'
SOCIAL_AUTH_TWITTER_SECRET = 'gvFo077HELXaXvXole5sSrkhZhNYto2yHFY8duLUSlxYPNLbUJ'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')] # mysite project templates
#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'polls/templates')] # pools application templates

