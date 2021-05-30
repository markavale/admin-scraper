'''Use this for production'''
import os
import dj_database_url
from .base import *

DEBUG = False
ALLOWED_HOSTS += [ 'admin-scraper.herokuapp.com'] # PUT HERE YOUR DOMAIN NAME WHEN YOU DEPLOY YOUR WEB APP
SECRET_KEY = config('SECRET_KEY')#
WSGI_APPLICATION = 'base.wsgi.prod.application'

THIRD_PARTY_APPS += [
    'debug_toolbar',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_name',
#         'USER': 'db_user',
#         'PASSWORD': 'db_password',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
CORS_ALLOWED_ORIGINS = [
    'https://markanthonyvale.herokuapp.com',
    'https://admin-mav.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com'
    # 'http://localhost:8080',
    # 'http://localhost:8081',
    # 'http://localhost:3307',
    # 'http://localhost:3306'
]

CSRF_TRUSTED_ORIGINS = [
    'https://admin-scraper.herokuapp.com',
    #'https://markanthonyvale.herokuapp.com', # 
    #'https://admin-mav.herokuapp.com', # 
]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = [
    'https://admin-scraper.herokuapp.com',
] 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'dist' ], # BASE_DIR / 'templates' depends on frontend => build
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

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATIC_URL = '/static/'
# Place static in the same location as webpack build files
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'dist/static'
    ]


##########
# STATIC #
##########

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#HTTPS Redirect
# settings.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SECURE_SSL_REDIRECT = True
# not sure yet
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


'''
    ENV VARIABLES SECTION
'''
TESTING = False