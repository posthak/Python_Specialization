"""
Задание №2.
    Создайте функцию аналог get для словаря.
    Помимо самого словаря функция принимает ключ и
значение по умолчанию.
    При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
    Реализуйте работу через обработку исключений.
"""


def custom_get(dictionary, key, default_value=0):
    try:
        return dictionary[key]
    except KeyError as e:
        print(f'Ключа {e} нет в словаре ')
        return default_value


