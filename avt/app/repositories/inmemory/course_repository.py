from ...entities.course import CourseEntity
from .base import InMemoryRepository


class InMemoryCourseRepository(InMemoryRepository[CourseEntity]):
    def get_course_by_tid(self, teacher_id: int) -> list[CourseEntity]:
        return [c for c in self._items.values() if c.teacher_id == teacher_id]