from ...entities.enrollment import EnrollmentEntity
from .base import InMemoryRepository


class InMemoryEnrollmentRepository(InMemoryRepository[EnrollmentEntity]):
    def list_by_user(self, user_id: int) -> list[EnrollmentEntity]:
        return [e for e in self._items.values() if e.user_id == user_id]