from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование только автору объекта.
    Остальным — только чтение.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user