from rest_framework import permissions
from login.models import User

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method == 'GET':
            if isinstance(request.user, User):
                return obj.owner == request.is_user
            return False
        return True