from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m$4t-dic+gzn*-deptvc6prdy&t1c*$v6@6xutv%j_yew^=*mh'


if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront1',
        'USER': 'root',
        'PASSWORD': 'Janeson16@x',
        'HOST': '127.0.0.1',
        'PORT': '3306',

    }
}
