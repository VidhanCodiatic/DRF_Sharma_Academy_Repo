
from rest_framework import permissions

class CustomUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        if request.method == 'POST':
            return True
        # for superuser only
        elif request.user.is_superuser == True:
            return True

        return False


# class CustomUserPermission(permissions.BasePermission):

#         def has_permissions(self, request, view):
#             """
#             Instantiates and returns the list of permissions that this view requires.
#             """
#             #   if self.action == 'list':
#             #       permission_classes = [permissions.IsAuthenticated]
#             if self.action == 'create':
#                 permission_classes = [permissions.AllowAny]
#             else:
#                 permission_classes = [permissions.IsAdminUser]
#             return [permission() for permission in permission_classes]