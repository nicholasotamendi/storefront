import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.dev')

celery = Celery('storefront') #name of the celery instance
celery.config_from_object('django.conf:settings', namespace='CELERY') #where to find the celery settings. Namespace tells celery to look for settings that start with CELERY_
celery.autodiscover_tasks() #to automatically discover tasks in the installed apps


