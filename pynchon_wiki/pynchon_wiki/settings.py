import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from factory import Faker

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '../infra/.env'))

SECRET_KEY = os.getenv('SECRET_KEY', 'test-key')
DEBUG = bool(os.getenv('DEBUG', False))
TEMPLATE_DEBUG = bool(os.getenv('TEMPLATE_DEBUG', False))
ALLOWED_HOSTS = str(os.getenv('ALLOWED_HOSTS', '*')).split()

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'wiki.apps.WikiConfig',
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'ckeditor',
    'import_export',
    'captcha'
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

ROOT_URLCONF = 'pynchon_wiki.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'pynchon_wiki.wsgi.application'

DATABASES = {
    'dev': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'production': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    },
}

DB_LOCAL = bool(os.getenv('DB_LOCAL', False))
DATABASES['default'] = DATABASES['dev' if DB_LOCAL else 'production']

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 1200,
        'autoParagraph': False,
        # 'forcePasteAsPlainText': True,
        'allowedContent': True,
        'extraPlugins': 'tabletools',
        'autoGrow_minHeight': 200,
        'autoGrow_maxHeight': 600,
        'autoGrow_bottomSpace': 50,
        'enterMode': 2,
        'shiftEnterMode': 1,
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'

DEFAULT_NAME_LENGTH = 255

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

THUMBNAIL_MEDIA_URL = '/media/'
THUMBNAIL_DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'wiki:index'
LOGOUT_REDIRECT_URL = 'wiki:index'

LOG_DIR = os.path.join(BASE_DIR, 'logs')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE_NAME = f'{LOG_DIR}/log-{datetime.today().strftime("%Y-%m-%d")}.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filters': ['require_debug_false'],
            'filename': LOG_FILE_NAME,
            'formatter': 'verbose'
        },
        'console': {
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    }
}

Faker._DEFAULT_LOCALE = 'ru_RU'

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_RECIPIENT = os.getenv('EMAIL_RECIPIENT')

CAPTCHA_IMAGE_SIZE = (150, 40)
CAPTCHA_FONT_SIZE = 35
