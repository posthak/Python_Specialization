"""
Задание No3
📌 Добавьте к задачам 1 и 2 строки документации для классов.
"""

import os
import pwd
import time


class MyStr:
    """Добавьте к задачам 1 и 2 строки документации для классов"""
    def __init__(self, text: str):
        """Add the parameters"""
        self.author = pwd.getpwuid(os.getuid())[0]
        self.times = time.time()
        self.text = text

    def get_text(self):
        """Get the text"""
        return self.text


f1 = MyStr('hello all!')
help(MyStr)
print(f'Документация класса: {MyStr.__doc__ = }')
print(f'Автор строки: {f1.author}')
print(f'Время создания:  {f1.times}')
print(f'Моя Строка: {f1.get_text().capitalize()}')
