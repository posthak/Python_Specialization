"""""
Задание No5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""""


class Rectangle:

    def __init__(self, side_a, side_b=0):
        self._side_a = side_a
        if side_b == 0:
            side_b = side_a
        self._side_b = side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        result = self.get_perimeter() + other.get_perimeter()
        return result

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __str__(self):
        return 'Rect'

rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)

print(f'Периметр прямоугольника = {rectangle1.get_perimeter():.2f}, \n'
      f'Площадь прямоугольника = {rectangle1.get_area():.2f}')
print(f'Периметр прямоугольника = {rectangle2.get_perimeter():.2f}, \n'
      f'Площадь прямоугольника = {rectangle2.get_area():.2f}')
obj = rectangle1 + rectangle2
# print(obj.result)

print(rectangle1 + rectangle2)
# print(rectangle1.__add__(rectangle2))
print(rectangle1 - rectangle2)

