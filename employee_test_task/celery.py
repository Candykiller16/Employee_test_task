import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_test_task.settings')

celery_app = Celery('employee_test_task')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'add-salary-every-2-hours': {
        'task': 'employees.tasks.send_money',
        'schedule': crontab(minute=0, hour='*/2'),
    },
}
