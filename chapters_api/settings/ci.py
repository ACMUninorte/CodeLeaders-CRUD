from datetime import timedelta

from .base import *

DEBUG = True

SECRET_KEY = "_"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "github_actions",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
