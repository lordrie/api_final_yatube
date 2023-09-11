from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Позволяет только автору объекта редактировать и удалять его."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
