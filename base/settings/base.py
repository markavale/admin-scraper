from pathlib import Path
# import os
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
LOCAL_APPS = [
    'users.apps.UsersConfig',
    'analytics.apps.AnalyticsConfig',
    'marketing.apps.MarketingConfig',
    'scraper.apps.ScraperConfig'
]
THIRD_PARTY_APPS = [
    'dj_rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'taggit',
    'taggit_serializer',
    'corsheaders',
    # 'debug_toolbar',
    # 'django_filters'

]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', # cors headers
    'corsheaders.middleware.CorsPostCsrfMiddleware', # trusted sites
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



# DJANGO RESTFRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}

# DJ REST AUTH CONF
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_LOGOUT_ON_GET = True


#'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'users.serializers.CustomLoginSerializer',
    'USER_SERIALIZER': 'users.serializers.UserSerializer',
    'REGISTER_SERIALIZER': 'users.serializers.RegisterUserSerializer',
    'PASSWORD_RESET_SERIALIZER ': 'users.serializers.CustomPasswordResetSerializer'
}


ROOT_URLCONF = 'base.urls'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='localhost')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# Rest auth conf
CSRF_COOKIE_NAME = "csrftoken"

# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'username'
# ACCOUNT_EMAIL_VERIFICATION = 'none'

# CUSTOM USER MODEL CONFIGS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'users.User'

# DJANGO-ALLAUTH CONFIGS
#authentication backends REQURED!!!
AUTHENTICATION_BACKENDS = (
   "django.contrib.auth.backends.ModelBackend",
#    'django.contrib.auth.backends.AllowAllUsersModelBackend',
#    "allauth.account.auth_backends.AuthenticationBackend"
)

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'
# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_SIGNUP_REDIRECT_URL  = '/login'
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


