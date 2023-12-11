"""""
Задание No1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)
"""""
import os
import pwd
import time


class MyStr:
    def __init__(self, text: str):
        self.author = pwd.getpwuid(os.getuid())[0]
        self.times = time.time()
        self.text = text

    def get_text(self):
        return self.text


f1 = MyStr('hello all!')
print(f'Автор строки: {f1.author}')
print(f'Время создания:  {f1.times}')
print(f'Моя Строка: {f1.get_text().capitalize()}')


class MyStr(str):
    def __new__(cls, text):
        instance = super().__new__(cls, text)
        instance.author = pwd.getpwuid(os.getuid())[0]
        instance.times = time.time()
        return instance



