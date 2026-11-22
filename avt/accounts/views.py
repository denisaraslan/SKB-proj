from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.container import auth_service, user_repo
from accounts.DB.users_option import UserRole

from .auth import role_required
from .serializers import LoginSerializer, RegisterSerializer, UserOutputSerializer, AdminCreateUserSerializer, ChangeRoleSerializer

ANY_ROLE = role_required(UserRole.STUDENT, UserRole.TEACHER, UserRole.ADMIN)
ADMIN_ONLY = role_required(UserRole.ADMIN)


def user_to_dict(user):
    return {
        "id": user.id,
        "email": user.email,
        "name": user.user_name,
        "role": user.role,
        "created_at": user.time_create.isoformat(),
    }


class RegisterView(APIView):
    def post(self, request):
        s = RegisterSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = auth_service.register(**s.validated_data)
        return Response(UserOutputSerializer(user).data, status=status.HTTP_201_CREATED)

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
    permission_classes = [ADMIN_ONLY]

    def get(self, request):
        return Response(UserOutputSerializer(auth_service.list_users(), many=True).data)

    def post(self, request):
        s = AdminCreateUserSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        d = s.validated_data
        user = auth_service.create_user(d["email"], d["name"], d["password"], d["role"])
        return Response(UserOutputSerializer(user).data, status=status.HTTP_201_CREATED)


class AdminUserDetailView(APIView):
    permission_classes = [ADMIN_ONLY]

    def get(self, request, user_id):
        return Response(UserOutputSerializer(auth_service.get_user(user_id)).data)

    def patch(self, request, user_id):
        s = ChangeRoleSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = auth_service.change_role(request.user.id, user_id, s.validated_data["role"])
        return Response(UserOutputSerializer(user).data)

    def delete(self, request, user_id):
        auth_service.delete_user(request.user.id, user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)