from celery import shared_task
from .models import EmployeeMPTT


@shared_task
def send_money():
    for i in EmployeeMPTT.objects.all():
        i.add_salary()
        i.save()
    return 'Money!!!'
