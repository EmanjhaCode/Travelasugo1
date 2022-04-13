"""
server file LOCATION
/var/www/djangomac/home
Django settings for emanjha project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
for open mongo server  : ./bin/mongod --dbpath=/Users/tabishadnan/data
old insert form : http://www.emanjha.com/emanjha/form.html
read write permision allow sudo chmod -R 757 blog
"""

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
import logging
from sentry_sdk.integrations.logging import LoggingIntegration
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)
sentry_sdk.init(
    dsn="https://5f6fd27d667a48aba3ecb80d9b61eb74@o984736.ingest.sentry.io/5940744",
    integrations=[DjangoIntegration(),sentry_logging],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True

)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(@ga8#lat^vm@6$^()8#2^y(s6g$#r%92d@iw_g(ybi@ijo8s9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emanjha_admin',
    'rest_framework',
    'corsheaders',
    'home',
    'mathfilters',
    'import_export',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:3000/',
# )
ROOT_URLCONF = 'emanjha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'emanjha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'djongo',
        'NAME': 'emanjha_admin',
    },
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
#media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tabishadnan9@gmail.com'
EMAIL_HOST_PASSWORD = 'viidiytcizvoxadx'
DEFAULT_FROM_EMAIL = 'Team Emanjha <noreply@emanjha.com>'

CACHES = {
'default':{
'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
'LOCATION' : '../home/cachetable',

}
}
IMPORT_EXPORT_USE_TRANSACTIONS = False
import os

LOGGING ={
    'version':1,
    'loggers':{
        'django':{
            'handlers':['file','file2'],
            'level':'DEBUG'
        }
    },
    'handlers':{
        'file':{
            'level':'INFO',
            'class': 'logging.FileHandler',
            'filename':'./logs/logfile_new.log',
            'formatter':'simpleRe',
        },
        'file2':{
            'level':'DEBUG',
            'class': 'logging.FileHandler',
            'filename':'./logs/debug6.log',
            'formatter':'simpleRe',
        }
    },
    'formatters':{
        'simpleRe': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        }

    }
}
