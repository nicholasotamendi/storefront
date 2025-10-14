from .common import *
import os
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('POSTGRES_URL'), 
        conn_max_age=600, 
        ssl_require=True
    )
}

ALLOWED_HOSTS = [os.environ.get('VERCEL_URL')]