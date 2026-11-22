# from django.http import JsonResponse
# from rest_framework.response import Response

from accounts.DB.users_option import UserRole, User
from app.entities.user import UserEntity
from app.security import verify_password
from app.exc import EmailAlreadyRegistered, InvalidCredentials, CannotModifySelf, UserNotFound
from accounts.DB.repositories.user_rep import UserRepository
# class AuthService:
#
#
#     def __init__(self, users:InMemoryUserRepository):
#         self.users = users
#
#     def create_user(self, email:str, name:str, password:str, role: UserRole) -> UserEntity:
#         email = email.lower().strip()
#
#         if self.users.get_by_email(email):
#             raise EmailAlreadyRegistered()
#
#         user = UserEntity(
#             id=0,  # тут 0 ибо настоящий id выдаст репозиторий когда его сохранит
#             email=email,
#             name=name,
#             role=role,
#             hashed_password=hash_password(password),
#             created_at=datetime.now(),
#         )
#
#         return self.users.add(user)
#
#     def register(self, email:str, name:str, password:str):
#         # Публичная регистрация всегда создаёт ученика
#         return self.create_user(email, name, password, UserRole.STUDENT)
#
#     def login(self, email: str, password: str) -> UserEntity:
#         user = self.users.get_by_email(email.strip())
#         if user is None or not verify_password(password, user.hashed_password):
#             raise InvalidCredentials()
#         return user

class AuthService:
    def __init__(self, users: UserRepository):
        self.users = users

    def create_user(self, email: str, user_name: str, password: str, role: str) -> User:
        if self.users.get_by_email(email):
            raise EmailAlreadyRegistered()

        user = self.users.create_user(
            email=email,
            password=password,
            user_name=user_name,
            role=role
        )
        return user

    def register(self, email: str, name: str, password: str) -> User:
        # Публичная регистрация всегда создаёт ученика
        return self.create_user(email, name, password, UserRole.STUDENT)

    def login(self, email: str, password: str) -> UserEntity:
        user = self.users.get_by_email(email.strip())
        if user is None or not verify_password(password, user.hashed_password):
            raise InvalidCredentials()
        return user

    def list_users(self):
        return self.users.list_all()

    def get_user(self, user_id: int):
        user = self.users.get_by_id(user_id)
        if user is None:
            raise UserNotFound()
        return user

    def change_role(self, actor_id: int, user_id: int, role: str):
        if actor_id == user_id:
            raise CannotModifySelf()
        return self.users.set_role(self.get_user(user_id), role)

    def delete_user(self, actor_id: int, user_id: int) -> None:
        if actor_id == user_id:
            raise CannotModifySelf()
        self.users.delete(self.get_user(user_id))