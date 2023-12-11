
"""
Задание No4
📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста и для пользователя.
"""

import os
import pwd
import time


class Archive:
    archives: list = []
    archives2: list  = []

    def __init__(self, text: str, num: int):
        self.num = num
        self.text = text
        self.safe_to_archive(self.archives)
        self.safe_to_archive(self.archives2)

    def safe_to_archive(self, ar):
        ar.append(f'[{self.num}, {self.text}]')

    def __repr__(self):
        return f'Archive({self.archives})'

    def __str__(self):
        return f'Экземпляр класса User с именем "{self.archives}"'


f1 = Archive('T1', 111)
f1 = Archive('T3', 333)
f2 = Archive('T2', 222)
print(repr(f1))
print(f1)
