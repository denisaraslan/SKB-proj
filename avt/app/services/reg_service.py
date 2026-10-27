from datetime import datetime

from app.entities.user import UserEntity, UserRole
from app.repositories.inmemory.user_rep import InMemoryUserRepository
from app.security import hash_password, verify_password

#потом
class EmailAlreadyRegistered(Exception):
    pass

#потом
class InvalidCredentials(Exception):
    pass

class AuthService:
    def __init__(self, users:InMemoryUserRepository):
        self.users = users

    def create_user(self, email:str, name:str, password:str, role: UserRole) -> UserEntity:
        email = email.lower().strip()

        if self.users.get_by_email(email):
            raise EmailAlreadyRegistered()

        user = UserEntity(
            id=0,  # тут 0 ибо настоящий id выдаст репозиторий когда его сохранит
            email=email,
            name=name,
            role=role,
            hashed_password=hash_password(password),
            created_at=datetime.now(),
        )

        return self.users.add(user)

    def register(self, email:str, name:str, password:str):
        # Публичная регистрация всегда создаёт ученика
        return self.create_user(email, name, password, UserRole.STUDENT)

    def login(self, email: str, password: str) -> UserEntity:
        user = self.users.get_by_email(email.strip())
        if user is None or not verify_password(password, user.hashed_password):
            raise InvalidCredentials()
        return user

