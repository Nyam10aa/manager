import os
from .base import *

#####################
# Security settings #
#####################

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'NAME': os.environ['DB_NAME'],
        'PORT': os.environ['DB_PORT'],
    }
}

################
# Static files #
################
GS_BUCKET_NAME = os.environ['STORAGE_BUCKET']
# STATIC_URL = '/static/'
STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(GS_BUCKET_NAME)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

################
# Media files #
################

MEDIA_URL = 'https://storage.googleapis.com/{}/media/'.format(GS_BUCKET_NAME)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, os.environ['STORAGE_CREDENTIAL']),
)

##################
# Email settings #
##################

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587

# EMAIL_CONFIG = env.email_url('EMAIL_URL')
# vars().update(EMAIL_CONFIG)

###################
# Stripe settings #
###################

# STRIPE_API_KEY = os.environ['STRIPE_API_KEY']
# STRIPE_PUBLISHABLE_KEY = os.environ['STRIPE_PUBLISHABLE_KEY']