# from rest_framework.permissions import permissions
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
         if request.method in BasePermission.SAFE_METHODS:
            return True
class IsDoctorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.role == 'doctor'
        return request.method in BasePermission.SAFE_METHODS
