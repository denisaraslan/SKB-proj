
from ...entities.lesson import LessonEntity
from .base import InMemoryRepository


class InMemoryLessonRepository(InMemoryRepository[LessonEntity]):
    def list_by_course(self, course_id: int) -> list[LessonEntity]:
        lessons = [l for l in self._items.values() if l.course_id == course_id]
        return sorted(lessons, key=lambda l: l.order)