class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows  # (int): Количество строк в матрице.
        self.cols = cols  # (int): Количество столбцов в матрице.
        self.data =  [[0 for j in range(cols)] for i in range(rows)]

    def __repr__(self):
        return f"Matrix('{str(self.rows)} , {str(self.cols)}')"

    def __str__(self):
        lines = []
        for row in self.data:
            lines.append(' '.join(str(x) for x in row))
        return '\n'.join(lines)

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        result = Matrix(self.rows,self.cols)
        for k in range(self.rows):
            for c in range(self.cols):
                result.data[k][c] = self.data[k][c] + other.data[k][c]
        return result

    def __mul__(self, other):
        result = Matrix(self.rows,self.cols)
        for k in range(self.rows):
            for c in range(self.cols):
                result.data[k][c] = self.data[k][c] * other.data[k][c]
        return result


# Создаем матрицы
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]
#
# Выводим матрицы
print(matrix1)

print(matrix2)

# Сравниваем матрицы
print(matrix1 == matrix2)

# Выполняем операцию сложения матриц
matrix_sum = matrix1 + matrix2
print(matrix_sum)


# Выполняем операцию сложения матриц
matrix_mul = matrix1 * matrix2
print(matrix_mul)
# import time
#
#
# class MyStr(str):
#     # def __init__(self, value, author):
#     #     self.author = author
#     #     self.value = value
#
#     def __new__(cls, value, author):
#         instance = super().__new__(cls, value)
#         # print(instance)
#         instance.author = author
#         instance.time = time.strftime("%Y-%m-%d %H:%M")
#         return instance
#
#     def __str__(self):
#         # return str.__str__(self + ' (Автор: ' + self.author + ', Время создания: ' + self.time + ')')
#         return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"
#
#     def __repr__(self):
#         return f"MyStr('{super().__str__()}', '{self.author}')"

#
# class Archive:
#     _instance = None
#     archive_text = []
#     archive_number = []
#
#     def __init__(self, text, number):
#         self.text = text
#         self.number = number
#         self.archive_number.append(number)
#         self.archive_text.append(text)
#
#     def __new__(cls, text, number):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __repr__(self):
#         return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'
#
# arc = Archive("Запись 1", 42)
# print(arc)
# print(id(arc))
# arc2 = Archive("Запись 2", 43)
# print(arc2)
# print(id(arc2))

#
# from typing import Union
#
# class Archive:
#     _instance = None
#     archive_text = []
#     archive_number = []
#
#     def __new__(cls, text: str, number: Union[int, float]):
#         if cls._instance is None:
#             cls._instance = super(Archive, cls).__new__(cls)
#             cls.archive_text = []
#             cls.archive_number = []
#             return cls._instance
#         return cls._instance
#
#     def __init__(self, text: str, number: Union[int, float]):
#         self.text = text
#         self.number = number
#         Archive.archive_text.append(self.text)
#         Archive.archive_number.append(self.number)
#
#     def __repr__(self):
#         return f'Text is {self.text} and number is {self.number}. ' \
#                f'Also {Archive.archive_text} and {Archive.archive_number}'
#
# archive1 = Archive("Запись 1", 42)
# print(archive1)
# print(id(archive1))
# archive2 = Archive("Запись 2", 3.14)
# print(archive2)
# print(id(archive2))

#
#
# class Rectangle:
#
#     def __init__(self, width, height=0):
#         self.width = width
#         if height == 0:
#             height = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __add__(self, other):
#         return Rectangle(self.width + other.width, self.height + other.height)
#
#     def __sub__(self, other):
#         return Rectangle(self.width - other.width, self.height - other.height)
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __le__(self, other):
#         return self.area() <= other.area()
#
#     def __str__(self):
#         return f'Прямоугольник со сторонами {self.width} и {self.height}'
#
#     def __repr__(self):
#         return f'Rectangle({self.width}, {self.height})'
#
# rect1 = Rectangle(4, 5)
# rect2 = Rectangle(3, 3)
#
# print(rect1)
# print(rect2)
#
# print(rect1.perimeter())
# print(rect1.area())
# print(rect2.perimeter())
# print(rect2.area())
#
# rect_sum = rect1 + rect2
# rect_diff = rect1 - rect2
#
# print(rect_sum)
# print(rect_diff)
#
# print(rect1 < rect2)
# print(rect1 == rect2)
# print(rect1 <= rect2)
#
# print(repr(rect1))
# print(repr(rect2))
