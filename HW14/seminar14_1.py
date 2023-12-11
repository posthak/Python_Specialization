"""
Задание No1
📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.
"""
import re


def del_symbols(text):
    return re.sub("[^A-Za-zА-яф-я ]", "", text).lower()


s = "Удал@ите# и*з тек^ста& все; с%имвол№ы№"

print(s)
print(del_symbols(s))
