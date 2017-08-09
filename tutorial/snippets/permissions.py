from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permit edit by owner only."""

    def has_object_permission(self, request, view, obj):
        """Allow GET, HEAD or OPTIONS request."""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
