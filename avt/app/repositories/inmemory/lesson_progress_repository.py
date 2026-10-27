from ...entities.lesson_progress import LessonProgressEntity
from .base import InMemoryRepository


class InMemoryLessonProgressRepository(InMemoryRepository[LessonProgressEntity]):
    def list_by_enrollment(self, enrollment_id: int) -> list[LessonProgressEntity]:
        return [p for p in self._items.values() if p.enrollment_id == enrollment_id]