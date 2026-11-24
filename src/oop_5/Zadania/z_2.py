'''
Обобщённая функция фильтрации
Реализуйте функцию, принимающую коллекцию и предикат (функцию, возвращающую bool).
Функция должна возвращать коллекцию того же типа,
содержащую только элементы, удовлетворяющие предикату.
'''
from typing import TypeVar, Callable, Iterable, List, Tuple, Set

T = TypeVar('T', bound=Iterable)
E = TypeVar('E')


def filter_collection(collection: T, predicate: Callable[[E], bool]) -> T:

    collection_type = type(collection)

    filtered_items = [item for item in collection if predicate(item)]

    if isinstance(collection, tuple):
        return tuple(filtered_items)
    elif isinstance(collection, set):
        return set(filtered_items)
    elif isinstance(collection, list):
        return list(filtered_items)
    else:
        return filtered_items

is_even = lambda x: x % 2 == 0

my_list = [1, 2, 3, 4, 5, 6]
print(f"Список: {filter_collection(my_list, is_even)}")

my_tuple = (10, 15, 20, 25)
print(f"Кортеж: {filter_collection(my_tuple, is_even)}")

my_set = {1, 2, 3, 4, 5}
print(f"Множество: {filter_collection(my_set, is_even)}")