class Person:
    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_many_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)

class Address:
    def __init__(self, country, city, street):
        self.country = country or ''
        self.city = city or ''
        self.street = street or ''

    def say_address(self):
        return f'Адрес героя: {self.country}, {self.city},{self.street}'
class Weapon:
    def __init__(self, left_hand, right_hand):
        self.left_hand = left_hand or 'Клинок'
        self.right_hand = right_hand or 'Лук'
class Hero(Person, Address, Weapon):
    def __init__(self, power, name=None, race=None, speed=None, country=None, city=None, street=None, left_hand=None, right_hand=None):
        self.power = power
        Person.__init__(self, name, race, speed)
        Address.__init__(self, country, city, street)
        Weapon.__init__(self, left_hand, right_hand)

    def change_health(self, other, quantity):
        self.health += quantity * 2
        other.health -= quantity * 2

    def add_many_ups(self):
        self.up += 1
        self.up = min(self.up, self._Person__max_up * 2)

p1 = Hero('archery', 'Сильвана', 'Эльф', 120,
          country='Эльфляндия', street='Ночного эльфа',
          left_hand='Стрела')

print(f'{p1.say_address()}')
print(f'{p1.right_hand = }, {p1.left_hand = }')


# class Person:
#     __max_up = 3
#     _max_level = 80
#
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
#
# p1 = Person('Сильвана', 'Эльф', 120)
# print(f'{p1.up = }')
# p1.up = 1
# print(f'{p1.up = }')
# for _ in range(5):
#     p1.add_up()
#     print(f'{p1.up = }')
# print(p1.__Person_max_up) # AttributeError: 'Person' object has no attribute '__max_up'
# print(Person.__max_up) # AttributeError: type object 'Person' has no attribute '__max_up'
#

# class User:
#     count = []
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
# u1 = User('One', '123-45-67')
# u2 = User('NoOne', '76-54-321')
# u1.count.append(42)
# u1.count.append(73)
# u2.counter = 256
# u2.count.append(u2.counter)
# u2.count.append(u1.count[-1])
# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')


# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#     def level_up(self):
#         self.level += 1
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }, {p3.health = }')
