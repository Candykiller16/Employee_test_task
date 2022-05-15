from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('index', index),
    path('', EmployeeListView.as_view()),
    path('<int:pk>/', EmployeeDetailView.as_view()),
    re_path('^employee-level/(?P<level>.+)/$', EmployeeRoleList.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
]
