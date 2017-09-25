from rest_framework import permissions


class IsPostOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    safe_methods = ('POST',)
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        return request.method in self.safe_methods