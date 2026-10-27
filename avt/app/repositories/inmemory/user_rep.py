from app.entities.user import UserEntity
from .base import InMemoryRepository

class InMemoryUserRepository(InMemoryRepository[UserEntity]):
    def get_by_email(self, email: str) -> UserEntity | None:
        email = email.lower()
        return next(
            (u for u in self._items.values() if u.email.lower() == email),
            None,
        )