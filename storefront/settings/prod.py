from .common import *
import os
import dj_database_url
from pathlib import Path

DEBUG = False

# Secret key comes from Vercel environment
SECRET_KEY = os.environ['SECRET_KEY']

# Try Neon/Vercel database URL first
POSTGRES_URL = os.environ.get('POSTGRES_URL') or os.environ.get('POSTGRES_POSTGRES_URL')

# Database configuration
if POSTGRES_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=POSTGRES_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # Fallback for local or build environment
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Allow both vercel and local
ALLOWED_HOSTS = [
    os.environ.get('VERCEL_URL', '127.0.0.1'),
    '.vercel.app',
    'localhost',
]
