import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_test_task.settings')

celery_app = Celery('employee_test_task')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()