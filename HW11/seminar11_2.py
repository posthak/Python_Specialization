"""""
Задание No2
📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков- архивов
📌 list-архивы также являются свойствами экземпляра
"""""

import os
import pwd
import time


class Archive:
    archives = []
    archives_2 = []

    def __init__(self, text, num):
        self.num = num
        self.text = text
        self.safe_to_archive(self.archives)
        self.safe_to_archive(self.archives_2)

    def safe_to_archive(self, ar):
        ar.append(f'{self.num}, {self.text}')

    def __str__(self):
        return 'Hi how are you'

    def __repr__(self):
        return 'Today the Weather is good!'

    def __add__(self, other):
        return Archive(self.text + other.text, self.num + other.num)


f1 = Archive('T1', 111)
print(f1.archives)

f2 = Archive('T2', 222)
print(f2.archives)

print(f1 + f2)
print(repr(f1))
