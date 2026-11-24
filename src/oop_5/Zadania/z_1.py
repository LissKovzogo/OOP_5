'''
Проверка аннотаций для кортежа
Создайте функцию:
def pair(values: tuple[str, int]) -> str:
    return f"{values[0]} — {values[1]}"
Перед вызовом убедитесь, что первый элемент кортежа — строка,
а второй — целое число.Выведите результат проверки.
'''
def pair(values: tuple[str, int]) -> str:
    return f"{values[0]} — {values[1]}"


def run_check(test_tuple: tuple) -> str:
    is_first_str = isinstance(test_tuple[0], str)
    is_second_int = isinstance(test_tuple[1], int)

    print(f"Первый элемент — строка: {is_first_str}")
    print(f"Второй элемент — целое число: {is_second_int}")

    if is_first_str and is_second_int:
        result = pair(test_tuple)
        print(f"Результат: {result}")
        return result
    else:
        print("Ошибка: типы данных не соответствуют аннотации.")
        return "Ошибка"

if __name__ == "__main__":
    test_tuple = ("Возраст", 25)
    run_check(test_tuple)