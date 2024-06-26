from project.environment import ENV
from pathlib import Path
import dj_database_url

from datetime import timedelta

# import json
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# with open("/home/zxl/dev/projects/python/django/dj_api/config.json","r") as config_file:
#     my_key = json.load(config_file).get("SECRET_KEY")
SECRET_KEY = ENV.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["127.0.0.1", "localhost","192.168.31.99"]


# Application definition

INSTALLED_APPS = [
    "rest_framework",
    'rest_framework_simplejwt',
    "admin_auto_filters",
    "admin_interface",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "common.apps.CommonConfig",
    "access.apps.AccessConfig",
    "content.apps.ContentConfig",
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


config = dj_database_url.config()
config["PASSWORD"] = ENV.str("POSTGRES_PASSWORD")
# DATABASES = {"default": config}
DATABASES = {
    # 'default': dj_database_url.config()
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dj_api',
        'USER': "postgres",
        'PASSWORD': "admin",
        'HOST': "localhost",
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# cache

REDIS_URL = ENV.str("REDIS_URL")


AUTH_USER_MODEL = "access.User"


REST_FRAMEWORK = {

    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],

    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ],
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PAGINATION_CLASS": "api.pagination.PageNumberPagination",
    "PAGE_SIZE": ENV.int("API_DEFAULT_PAGE_SIZE", default=10),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        seconds=ENV.int("AUTH_JWT_ACCESS_TOKEN_TIMEOUT", default=86400)
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        seconds=ENV.int("AUTH_JWT_REFRESH_TOKEN_TIMEOUT", default=604800)
    ),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": ENV.str("AUTH_JWT_SIGNING_KEY"),
    "USER_ID_FIELD": "uuid",
}

AUTH_TOKEN_TIMEOUT = ENV.int("AUTH_TOKEN_TIMEOUT", default=259200)
AUTH_TOKEN_SECRET = ENV.str("AUTH_TOKEN_SECRET")

API_DEFAULT_PAGE_SIZE = ENV.int("API_DEFAULT_PAGE_SIZE", default=10)
API_MAX_PAGE_SIZE = ENV.int("API_MAX_PAGE_SIZE", default=100)



