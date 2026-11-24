from typing import TypeVar, List

T = TypeVar("T")  # обобщённый тип

def first(items: List[T]) -> T:
    """Возвращает первый элемент списка любого типа."""
    return items[0]