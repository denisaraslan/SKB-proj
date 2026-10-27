from typing import Generic, TypeVar

T = TypeVar("T")


class InMemoryRepository(Generic[T]):
    """базовый склад: хранит сущности в словаре {id: сущность}."""

    def __init__(self):
        self._items: dict[int, T] = {}
        self._next_id = 1

    def add(self, entity: T) -> T:
        entity.id = self._next_id          # выдаём настоящий id
        self._items[entity.id] = entity
        self._next_id += 1
        return entity

    def get_by_id(self, entity_id: int) -> T | None:
        return self._items.get(entity_id)

    def list_all(self) -> list[T]:
        return list(self._items.values())

    def update(self, entity: T) -> T:
        if entity.id not in self._items:
            raise KeyError(f"Сущность с id={entity.id} не найдена")
        self._items[entity.id] = entity
        return entity

    def delete(self, entity_id: int) -> bool:
        return self._items.pop(entity_id, None) is not None