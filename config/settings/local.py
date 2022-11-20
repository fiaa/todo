import os

from .base import *  # noqa: F403
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "*"]

DATABASES["default"]["HOST"] = os.environ.get("DJANGO_DATABASE_HOST")  # noqa: F405
DATABASES["default"]["NAME"] = os.environ.get("DJANGO_DATABASE_NAME")  # noqa: F405
DATABASES["default"]["USER"] = os.environ.get("DJANGO_DATABASE_USER")  # noqa: F405
DATABASES["default"]["PASSWORD"] = os.environ.get(
    "DJANGO_DATABASE_PASSWD"
)  # noqa: F405
DATABASES["default"]["PORT"] = os.environ.get("DJANGO_DATABASE_PORT")  # noqa: F405

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa: F405

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "targetyo": {"handlers": ["console"], "level": "DEBUG", "propagate": False}
    },
}
