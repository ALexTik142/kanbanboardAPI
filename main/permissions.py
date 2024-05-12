from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):        #Доступ на уровне всего запроса (безопасный всем, остальное для админа)
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsUserOrReadOnly(permissions.BasePermission):          #Доступ для отдельного объекта/записи (безопастный всем, остальное для пользователя который добавил запись)
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user