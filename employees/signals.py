from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import EmployeeMPTT


def create_employee(sender, instance, created, **kwargs):
    if created:
        employee = instance
        user = User.objects.create_user(
            username=employee.full_name,
        )
        # instance.user = user.username


def update_employee(sender, instance, created, **kwargs):
    employee = instance
    user = employee.user

    if created == False:
        user.first_name = employee.full_name
        user.save()


def delete_employee(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_employee, sender=EmployeeMPTT)
# post_save.connect(update_employee, sender=User)
# post_delete.connect(delete_employee, sender=EmployeeMPTT)
