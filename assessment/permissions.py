
from rest_framework import permissions

class CustomAssessmentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # for superuser only
        if request.user.is_superuser== True:
            return True
        elif request.user.is_staff == True:
            return True
        elif request.user.is_active == True:
            return request.method in permissions.SAFE_METHODS
        return False
    