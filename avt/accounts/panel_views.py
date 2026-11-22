from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie

from accounts.DB.users_option import UserRole
from app.container import user_repo


@ensure_csrf_cookie            # выдаёт браузеру csrf-cookie для проверки
def admin_panel(request):
    user_id = request.session.get("user_id")
    user = user_repo.get_by_id(user_id) if user_id is not None else None
    if user is None:
        return redirect("/login")
    if user.role != UserRole.ADMIN:
        return HttpResponseForbidden("Нет доступа")
    return render(request, "acc/admin_panel.html", {"admin_email": user.email})