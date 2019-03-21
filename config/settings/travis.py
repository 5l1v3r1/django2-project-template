from .base import *  # noqa pylint: disable=E0401

SECRET_KEY = 'fake-key'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}

PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)

MIGRATION_MODULES = {'baseapp': None}
