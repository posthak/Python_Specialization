import json


class User:
    def __init__(self, name: str, user_id: str, level: str = '0') -> None:
        self.name = name
        self.user_id = user_id
        self.level = level


class BasedExep(Exception):
    pass


class NameErr(BasedExep):
    pass


class LevelErr(BasedExep):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка уровня"


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
        # try:
        for el in CheckUserLogin.users:
            if name == el.name:
                return 'Пользователь найден'
            raise NameErr()
        # except NameErr as e:
        #     return 'Пользователь не найден'
