from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.container import auth_service, user_repo
from app.entities.user import UserRole

from .auth import role_required
from .serializers import LoginSerializer, RegisterSerializer

ANY_ROLE = role_required(UserRole.STUDENT, UserRole.TEACHER, UserRole.ADMIN)


def user_to_dict(user):
    return {
        "id": user.id,
        "email": user.email,
        "name": user.name,
        "role": user.role.value,
        "created_at": user.created_at.isoformat(),
    }


class RegisterView(APIView):
    def post(self, request):
        s = RegisterSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = auth_service.register(**s.validated_data)
        return Response(user_to_dict(user), status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        s = LoginSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = auth_service.login(**s.validated_data)
        request.session["user_id"] = user.id
        return Response(user_to_dict(user))


class LogoutView(APIView):
    def post(self, request):
        request.session.flush()                # стираем сессию
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeView(APIView):
    permission_classes = [ANY_ROLE]

    def get(self, request):
        return Response(user_to_dict(request.user))


class AdminUsersView(APIView):
    permission_classes = [role_required(UserRole.ADMIN)]

    def get(self, request):
        return Response([user_to_dict(u) for u in user_repo.list_all()])