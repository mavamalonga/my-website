from rest_framework.permissions import BasePermission, SAFE_METHODS


class StaffPermission(BasePermission):
    message = 'Permission only to the staff member.'

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        return request.user.is_staff == True

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        return request.user.is_staff == True