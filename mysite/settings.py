"""
Django settings for django-polls-app project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
# Checks using python3 manage.py migrate
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# Updated the database to use mysql instead of sqlite3 in order to use the database on the server and continuously update it without any issues
# You must use the environment variables to store the database credentials
# Then use the export command to set the environment variables in the terminal or command prompt for what you have set as the respective credentials
DATABASES = {
    # 'default' is the key for the default database.
    'default': {
        # The ENGINE setting tells Django which database engine to use.
        # For MySQL, you should use 'django.db.backends.mysql'.
        'ENGINE': 'django.db.backends.mysql',

        # NAME is the name of your MySQL database.
        # It's fetched from environment variable 'DB_NAME'.
        'NAME': os.getenv('DB_NAME'),

        # USER is the username of the MySQL user who has access to the database.
        # It's fetched from environment variable 'DB_USER'.
        'USER': os.getenv('DB_USER'),

        # PASSWORD is the password of the MySQL user.
        # It's fetched from environment variable 'DB_PASSWORD'.
        'PASSWORD': os.getenv('DB_PASSWORD'),

        # HOST is the host where your MySQL server is running.
        # It's fetched from environment variable 'DB_HOST' with 'localhost' as default value.
        'HOST': os.getenv('DB_HOST'),

        # PORT is the port on which your MySQL server is listening.
        # It's fetched from environment variable 'DB_PORT' with '3306' as default value.
        'PORT': os.getenv('DB_PORT')
    }
    
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#updated the timezone to America/Chicago
#TIME_ZONE = 'UTC' is the default but for some reason creates an error on the server
TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'