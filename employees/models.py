from datetime import date

from django.contrib.auth.models import User
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class EmployeeMPTT(MPTTModel):
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SR_MANAGER = 'SR_MGR'
    BOSS = 'BS'
    PRESIDENT = 'PRES'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SR_MANAGER, 'senior manager'),
        (BOSS, 'boss'),
        (PRESIDENT, 'president'))

    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
    date_of_employment = models.DateField(default=date.today)
    salary_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    paid_salary_inf = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='employee', on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.__str__()

    def add_salary(self):
        self.paid_salary_inf = self.paid_salary_inf + self.salary_amount
        return self.paid_salary_inf

