from app.DB.users_option import User


class UserRepository:
    def get_by_id(self, user_id: int) -> User | None:
        return User.objects.filter(id=user_id).first()

    def get_by_email(self, email: str) -> User | None:
        return User.objects.filter(email__iexact=email).first()

    def get_users_by_role(self, role: str):
        return User.objects.filter(role=role)

    def create_user(self, email: str, password: str, user_name: str, role: str) -> User:
        return User.objects.create_user(email=email, password=password, user_name=user_name, role=role)