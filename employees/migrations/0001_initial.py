# Generated by Django 4.0.4 on 2022-05-08 00:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeMPTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('STD', 'base employee'), ('MGR', 'manager'), ('SR_MGR', 'senior manager'), ('BS', 'boss'), ('PRES', 'president')], max_length=25)),
                ('date_of_employment', models.DateField(default=datetime.date.today)),
                ('salary_amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('paid_salary_inf', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='employees.employeemptt')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
