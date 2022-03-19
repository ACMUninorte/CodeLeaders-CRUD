from datetime import timedelta

import dj_database_url
from decouple import config

from .base import *

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

db_from_env = dj_database_url.config(conn_max_age=600)

DATABASES = {"default": db_from_env}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = True
