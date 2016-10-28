from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to onely allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowerd to any request, so we'll always
        # allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed for the snippet owner
        return obj.owner == request.user
