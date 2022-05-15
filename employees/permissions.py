from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user.is_staff:
            return True


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            elif request.user.is_staff:
                return True
            else:
                return obj.user == request.user
        else:
            return False
