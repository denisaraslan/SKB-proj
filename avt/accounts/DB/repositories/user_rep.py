from accounts.DB.users_option import User


class UserRepository:
    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def get_by_email(email: str) -> User | None:
        return User.objects.filter(email__iexact=email).first()

    @staticmethod
    def get_users_by_role(role: str):
        return User.objects.filter(role=role)

    @staticmethod
    def create_user(email: str, password: str, user_name: str, role: str) -> User:
        return User.objects.create_user(email=email, password=password, user_name=user_name, role=role)