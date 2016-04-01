import os
import raven


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT_DIR = os.path.dirname(BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sx&6m6l+od7k5k_s^(cqvg4h4=)sn)&ic$r^n8-%6$)y5ibiw_'

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
    'photogram',
    'raven.contrib.django.raven_compat',

    'users',
    'posts',
    'tags',
]


RAVEN_CONFIG = {
    'dsn': 'https://eb5da71db4654faeab564001faa0edde:1cde857c28eb40bd880d7014714b5f38@app.getsentry.com/72473',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
}
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'photogram.urls'

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

WSGI_APPLICATION = 'photogram.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'users.User'
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, 'dist', 'media')
