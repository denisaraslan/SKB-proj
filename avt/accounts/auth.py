from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from app.container import user_repo


class SessionUserAuthentication(BaseAuthentication):
    """Определяет пользователя по id, сохранённому в сессии."""

    def authenticate(self, request):
        user_id = request.session.get("user_id")
        if user_id is None:
            return None                    # не вошёл
        user = user_repo.get_by_id(user_id)
        if user is None:
            return None                    # например, сервер перезапускали
        return (user, None)                # DRF положит (user, None)  в request


def role_required(*roles):
    #фабрика прав( пускает только пользователей с указанными ролями.)

    class _Permission(BasePermission):
        def has_permission(self, request, view):
            user = request.user
            return user is not None and user.role in roles

    return _Permission