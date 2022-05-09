from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, views
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import EmployeeMPTT
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsStaff, IsOwner


def index(request):
    return HttpResponse("<h1>It's working</h1>")


class EmployeeListView(generics.ListAPIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = EmployeeMPTT.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff, permissions.IsAdminUser]


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = EmployeeMPTT.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]


class EmployeeRoleList(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser, IsStaff]

    def get_queryset(self):
        level = self.kwargs['level']
        return EmployeeMPTT.objects.filter(level=level)
