'''Use this for development'''

from .base import *
# import os

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
DEBUG = True

WSGI_APPLICATION = 'base.wsgi.dev.application'

#DATABASES = {
#    'default': {
#    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#    'NAME': config('NAME_PS'),
#    'USER':config('USER_PS'),
#    'PASSWORD': config('PASSWORD_PS'),
#    'HOST': config('HOST_PS'),
#    'PORT': config('PORT_PS', cast=int),
#    }
#}

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
     }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'PORT':config('PORT', cast=int),
#         'HOST':config('HOST'),
#         #'SSL':
#     }
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'public' ], # BASE_DIR / 'templates' depends on frontend => build
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

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
    "http://127.0.0.1:3307"
    # 'http://localhost:3306',
    # 'http://localhost:3307'
]

CSRF_TRUSTED_ORIGINS = [
     "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
    "http://127.0.0.1:3307"
]
CORS_ALLOW_ALL_ORIGINS = True
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # it depends on frontend
STATIC_ROOT = BASE_DIR / 'staticfiles' # staticfiles for collecting static and for deploymen

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


'''
    @ ENV VARIABLES SECTION
'''
TESTING = True
