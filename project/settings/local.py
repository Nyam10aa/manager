import os
from .base import *

#####################
# Security settings #
#####################

DEBUG = True

SECRET_KEY = '<fake-secret-key>'

ALLOWED_HOSTS = ['*']

# it is for debug-toolbar
INTERNAL_IPS = []

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ['DB_HOST_dev'],
        'PORT': os.environ['DB_PORT_dev'],
        'NAME': os.environ['DB_NAME_dev'],
        'USER': os.environ['DB_USER_dev'],
        'PASSWORD': os.environ['DB_PASSWORD_dev'],
    }
}

################
# Static files #
################
GS_BUCKET_NAME = os.environ['STORAGE_BUCKET_dev']
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

# メールをコンソールに表示する
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER_dev']
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD =os.environ['EMAIL_HOST_PASSWORD_dev']

#################
# debug toolbar #
#################

if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )