from rest_framework.permissions import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
         if request.method in permissions.SAFE_METHODS:
            return True
class IsDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.role == 'doctor'
        return request.method in permissions.SAFE_METHODS
