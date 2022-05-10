from random import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed

from employees.models import EmployeeMPTT


class Command(BaseCommand):
    help = u'Add users'

    def handle(self, *args, **options):
        peter_user = User.objects.create_user(username='peter_griffin', email='', password='admin', is_superuser=True,
                                              is_staff=True)
        peter_griffin = EmployeeMPTT.objects.create(full_name='Peter Griffin', role=EmployeeMPTT.PRESIDENT,
                                                    user=peter_user)
        lois_user = User.objects.create_user(username='lois_griffin', email='', password='123')
        lois_griffin = EmployeeMPTT.objects.create(full_name='Lois Griffin', role=EmployeeMPTT.BOSS,
                                                   parent=peter_griffin, user=lois_user)

        brian_user = User.objects.create_user(username='brian_griffin', email='', password='123')
        brian_griffin = EmployeeMPTT.objects.create(full_name='Brian Griffin', role=EmployeeMPTT.SR_MANAGER,
                                                    parent=lois_griffin, user=brian_user)

        stewie_user = User.objects.create_user(username='stewie_griffin', email='', password='123')
        stewie_griffin = EmployeeMPTT.objects.create(full_name='Stewie Griffin', role=EmployeeMPTT.MANAGER,
                                                     parent=brian_griffin, user=stewie_user)

        chris_user = User.objects.create_user(username='chris_griffin', email='', password='123')
        chris_griffin = EmployeeMPTT.objects.create(full_name='Chris Griffin', role=EmployeeMPTT.STANDARD,
                                                    parent=stewie_griffin, user=chris_user)

        clevelend_user = User.objects.create_user(username='cleveland_brown', email='', password='123')
        cleveland_brown = EmployeeMPTT.objects.create(full_name='Cleveland Brown', role=EmployeeMPTT.BOSS,
                                                      parent=peter_griffin, user=clevelend_user)

        joe_user = User.objects.create_user(username='joe_swanson', email='', password='123')
        joe_swanson = EmployeeMPTT.objects.create(full_name='Joe Swanson', role=EmployeeMPTT.SR_MANAGER,
                                                  parent=cleveland_brown, user=joe_user)

        meg_user = User.objects.create_user(username='meg_griffin', email='', password='123')
        meg_griffin = EmployeeMPTT.objects.create(full_name='Meg Griffin', role=EmployeeMPTT.MANAGER,
                                                  parent=joe_swanson, user=meg_user)

        glenn_user = User.objects.create_user(username='glenn_quagmire', email='', password='123')
        glenn_quagmire = EmployeeMPTT.objects.create(full_name='Glenn Quagmire', role=EmployeeMPTT.STANDARD,
                                                     parent=meg_griffin, user=glenn_user)
        return 'Done'
