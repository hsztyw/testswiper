import os

from celery import Celery

from tasks import confg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ztc.settings")

celery_app = Celery('async_tasks')

celery_app.config_from_object(confg)

celery_app.autodiscover_tasks()
