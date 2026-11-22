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

    @staticmethod
    def list_all():
        return User.objects.order_by("id")

    @staticmethod
    def set_role(user, role) -> User:
        user.role = role
        user.save(update_fields=["role", "time_update"])
        return user

    @staticmethod
    def delete(user) -> None:
        user.delete()