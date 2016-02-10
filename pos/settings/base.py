"""
Django settings for pos project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from datetime import timedelta

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h!%$9w&o!o=4=dq&0o^tn*pb(y1k5e6r*a5wlsiwj98vi!)lxt'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'stronghold',
    'social.apps.django_app.default',
    'widget_tweaks',

    'pos.core',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'pos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pos.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# Presumes you have set up PG with 'ident sameuser':
# https://help.ubuntu.com/community/PostgreSQL#Alternative_Server_Setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pos',
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


AUTHENTICATION_BACKENDS = (
    'pos.core.backends.PebbleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = (
    'email',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

OPENID_URL = 'example.com'

# If this was the last link on the chain, then we go back to the master
# This is just a redirect, so you can pass in a server-local destination
MASTER_SERVER = 'http://example.com/'
MASTER_SERVER_LOGOUT = 'http://example.com/logout/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SUPPORT_EMAIL = 'support@mypebble.co.uk'
MARKETING_EMAIL = 'info@mypebble.co.uk'
PEBBLE_PHONE = '0845 310 1788'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = timedelta(days=1).total_seconds()

SITE_ID = 1

LOGIN_URL = '/social/login/pebble/'
LOGIN_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.TemplateHTMLRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'MAX_PAGINATE_BY': 1000,
    'PAGINATE_BY': 20,
    'PAGINATE_BY_PARAM': 'per_page',
}

# Let admin handle all this
STRONGHOLD_PUBLIC_URLS = (
    r'^/admin/',
    r'^/reset/',
    r'^/social/',
)

STRONGHOLD_PUBLIC_NAMED_URLS = (
    'login',
    'password-reset',
    'set-password',
    'password_reset-confirm',
    'password-reset-confirm',
    'password_reset_complete',
    'password_reset_done',
)

DEBUG = False

# use persistent db connection
# https://docs.djangoproject.com/en/1.9/ref/databases/#persistent-connections
CONN_MAX_AGE = 60

try:
    from .local_settings import *
except ImportError:
    pass
