import dj_database_url

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_value('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get_value('LOCAL_DB_NAME'),
        'USER': env.get_value('LOCAL_DB_USER'),
        'PASSWORD': env.get_value('LOCAL_DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
