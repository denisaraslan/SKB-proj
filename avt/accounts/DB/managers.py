from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, user_name: str, role: str):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            hashed_password=make_password(password),
            user_name=user_name,
            role=role,
        )
        user.save(using=self._db)
        return user