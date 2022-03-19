from datetime import timedelta

from decouple import config

from .base import *

DEBUG = True

SECRET_KEY = config("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
