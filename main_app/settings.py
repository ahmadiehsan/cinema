import json
import os
from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()
environ.Env.read_env()


def get_env_value(env_variable, default_value=None):
    try:
        return os.environ[env_variable]
    except KeyError:
        if env.get_value(env_variable):
            return env.get_value(env_variable)
        elif default_value:
            return default_value
        else:
            error_msg = 'Please set the {} environment variable'.format(env_variable)
            raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_value('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = json.loads(get_env_value('DEBUG', 'false'))

ALLOWED_HOSTS = get_env_value('ALLOWED_HOSTS', '*').replace(', ', ',').replace(' ,', ',').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main_app',
    'apps.user',
    'apps.shop',

    'django_node_assets',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main_app.urls'

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

WSGI_APPLICATION = 'main_app.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'  # TODO (ehsan) change it to UTC
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (BASE_DIR / 'locale',)

# DB and Cache
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_value('POSTGRES_DB_NAME'),
        'USER': get_env_value('POSTGRES_DB_USER'),
        'PASSWORD': get_env_value('POSTGRES_DB_PASSWORD'),
        'HOST': get_env_value('POSTGRES_DB_HOST'),
        'PORT': get_env_value('POSTGRES_DB_PORT'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'main_app' / 'static',
]
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_node_assets.finders.NodeModulesFinder',
]
NODE_PACKAGE_JSON = BASE_DIR / 'package.json'
NODE_MODULES_ROOT = BASE_DIR / 'node_modules'

# Dynamic files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth
AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/user/sign-in/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/user/sign-out/'
LOGOUT_REDIRECT_URL = '/user/sign-in/'

# Log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}\n',
            'style': '{'
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'WARNING',
        },
    },
    'loggers': {
        'suds': {
            'handlers': [],
            'propagate': True,
            'level': 'CRITICAL',
        },
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    },
}
