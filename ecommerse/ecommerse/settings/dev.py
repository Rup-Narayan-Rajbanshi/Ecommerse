from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default':{
        'ENGINE': config('DATABASE_ENGINE'),
        'NAME': config('DATABASE_NAME'),
    }
}


# DATABASES = {
#     'default':{
#         'ENGINE': config('DATABASE_ENGINE'),
#         'NAME': config('DATABASE_NAME'),
#         'USER': config('DATABASE_USER'),
#         'HOST': config('DATABASE_HOST'),
#         'PORT': config('DATABASE_PORT'),
#         'PASSWORD':config('DATABASE_PASSWORD'),
#     }
# }