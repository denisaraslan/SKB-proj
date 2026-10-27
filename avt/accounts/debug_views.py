from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from app.container import user_repo


def debug_users(request):
    # страница только для разработки: на проде (DEBUG=False) её как будто нет
    if not settings.DEBUG:
        raise Http404

    users = [
        {
            "id": u.id,
            "email": u.email,
            "name": u.name,
            "role": u.role.value,
            "created_at": u.created_at,
            # Показываем только начало хеша, чтобы видно было: пароль хранится в виде хеша
            "hash_preview": u.hashed_password[:30] + "…",
        }
        for u in user_repo.list_all()
    ]
    return render(request, "acc/debug_users.html", {"users": users})