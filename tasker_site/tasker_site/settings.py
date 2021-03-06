from pathlib import Path
from decouple import config

from datetime import timedelta

import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', cast=str)

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = [
    'localhost',
	'127.0.0.1',
]


INSTALLED_APPS = [
    # apps
	'tasker_frontend.apps.TaskerFrontendConfig',
	'graphql_api.apps.GraphqlApiConfig',
    
    # 3rd party apps
	'corsheaders',
	'graphene_django',
	'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
	'graphql_auth',
	'django_filters',
    
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

MIDDLEWARE = [
	# third party
	'corsheaders.middleware.CorsMiddleware',

	# django built-in
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tasker_site.urls'

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

WSGI_APPLICATION = 'tasker_site.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'content-disposition',
    'accept-encoding',
    'content-type',
    'accept',
    'origin',
    'authorization',
	'X-CSRFToken',
]

CORS_EXPOSE_HEADERS = ["X-CSRFTOKEN"]

GRAPHENE = {
    'SCHEMA': 'graphql_api.schema.schema',
    'MIDDLEWARE': [
    	'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
	'JWT_ALLOW_ANY_CLASSES': [
		'graphql_auth.mutations.Register',
		'graphql_auth.mutations.VerifyAccount',
		'graphql_auth.mutations.ObtainJSONWebToken',
	],
	'JWT_VERIFY_EXPIRATION': True,
	'JWT_EXPIRATION_DELTA': timedelta(minutes=999),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=999),
	'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
	'JWT_ALLOW_ARGUMENT': True,
}

AUTHENTICATION_BACKENDS = [
	'graphql_jwt.backends.JSONWebTokenBackend',
	'django.contrib.auth.backends.ModelBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
