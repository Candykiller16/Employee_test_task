from rest_framework import serializers
from .models import EmployeeMPTT


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMPTT
        fields = ['id', 'full_name', 'role', 'date_of_employment', 'salary_amount', 'paid_salary_inf',
                  'level', 'parent']
