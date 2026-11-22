from django.urls import path

from .views import AdminUsersView, LoginView, LogoutView, MeView, RegisterView, AdminUserDetailView
urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("me/", MeView.as_view()),
    path("admin/users/", AdminUsersView.as_view()),
    path("admin/users/<int:user_id>/", AdminUserDetailView.as_view()),
]