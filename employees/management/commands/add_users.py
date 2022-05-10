from random import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed

from employees.models import EmployeeMPTT


class Command(BaseCommand):
    help = u'Add users'

    def handle(self, *args, **options):
        peter_griffin = EmployeeMPTT.objects.create(full_name='Peter Griffin', role=EmployeeMPTT.PRESIDENT)
        lois_griffin = EmployeeMPTT.objects.create(full_name='Lois Griffin', role=EmployeeMPTT.BOSS,
                                                   parent=peter_griffin)
        brian_griffin = EmployeeMPTT.objects.create(full_name='Brian Griffin', role=EmployeeMPTT.SR_MANAGER,
                                                    parent=lois_griffin)
        stewie_griffin = EmployeeMPTT.objects.create(full_name='Stewie Griffin', role=EmployeeMPTT.MANAGER,
                                                     parent=brian_griffin)
        chris_griffin = EmployeeMPTT.objects.create(full_name='Chris Griffin', role=EmployeeMPTT.STANDARD,
                                                    parent=stewie_griffin)
        cleveland_brown = EmployeeMPTT.objects.create(full_name='Cleveland Brown', role=EmployeeMPTT.BOSS,
                                                      parent=peter_griffin)
        joe_swanson = EmployeeMPTT.objects.create(full_name='Joe Swanson', role=EmployeeMPTT.SR_MANAGER,
                                                  parent=cleveland_brown)
        meg_griffin = EmployeeMPTT.objects.create(full_name='Meg Griffin', role=EmployeeMPTT.MANAGER,
                                                  parent=joe_swanson)
        glenn_quagmire = EmployeeMPTT.objects.create(full_name='Glenn Quagmire', role=EmployeeMPTT.STANDARD,
                                                     parent=meg_griffin)
        return 'Done'
        # seeder = Seed.seeder()
        # seeder.add_entity(User, total, {
        #     'username': lambda x: seeder.faker.name(),
        #     'email': lambda x: seeder.faker.email(),
        #     'password': 'password123'
        # })
        # seeder.execute()
