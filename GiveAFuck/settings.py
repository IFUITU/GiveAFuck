"""
Django settings for GiveAFuck project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u+n_q2s2$o5a_rwp^ebrf2ic)_rj^=)+bdtie#20^+scf!f%(6'

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
    'django_crontab',
    'crispy_forms',
    'main',
    'debug_toolbar',
    'user'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'djangohmac.middleware.HmacMiddleware',
]

ROOT_URLCONF = 'GiveAFuck.urls'

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
                'django.template.context_processors.media',
                'GiveAFuck.globals.Platforms',
                'GiveAFuck.globals.crn',
                'GiveAFuck.globals.register_modal'
            ],
        },
    },
]

WSGI_APPLICATION = 'GiveAFuck.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "GiveAFuck",
        'HOST':'127.0.0.1',
        'USER':'root',
        'PASSWORD':'Qwerty123$'

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

INTERNAL_IPS = [
    '127.0.0.1'
]
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# HMAC_SECRET = 'HMAC_SECRET' #single key
# HMAC_SECRETS = {
#     'serviceA': 'HMAC_SERVICE_A_SECRET',
#     'serviceB': 'HMAC_SERVICE_B_SECRET'
# } #multiple keys


""" EXTRAP SETTINGS OF HMAC
        HMAC_HEADER: HTTP header where signature is stored (Default: Signature)
        HMAC_DIGESTMOD: Digest mod (Default: hashlib.sha256)
        HMAC_DISABLE: Disable or enable HMAC True/False (Default: Enabled)
"""


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'user.User'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

#CRONJOBS
CRONJOBS = [
    ('*/2 * * * *', 'main.cron.my_cron_job')
]

LOGIN_URL = '#myModal'
LOGIN_REDIRECT_URL = 'main:index'
