"""
Задание No5
📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет,
вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
"""
import json


class BasedExep(Exception):
    pass


class NameErr(BasedExep):
    pass


class LevelErr(BasedExep):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка уровня"


class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level


class CheckUserLogin:
    users = []

    # def __init__(self):
    @staticmethod
    def create_user(name, id, level):
        try:
            if level > 3:
                raise LevelErr(level)
        except LevelErr as e:
            print(e)
        else:
            obj = User(name, id, level)
            CheckUserLogin.users.append(obj)

    @staticmethod
    def load_users():
        with open('13.json', 'r', encoding='UTF-8') as js_f:
            user_dict = json.load(js_f)
            for level, user_list in user_dict.items():
                for id, name in user_list.items():
                    CheckUserLogin.users.append(User(name, id, level))

    @staticmethod
    def get_login_level(name):
        try:
            for el in CheckUserLogin.users:
                if name == el.name:
                    return 'Пользователь найден'
                raise NameErr()
        except NameErr as e:
            return 'Пользователь не найден'



if __name__ == "__main__":
    a = CheckUserLogin()
    a.load_users()
    print(len(a.users))
    a.create_user('Ivanov', '08', 2)
    print(len(a.users))
    print(a.get_login_level('Новиков'))
