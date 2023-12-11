import csv

"""
    Создать класс Студент с атрибутами и фукциями
    Создать дескриптор для проверки, что ФИО начинается с заглавной буквы
    Добавить логирования ошибок и логирования полезной информации
"""
class NameValidator:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        # instance.__dict__[self.param_name] = value
        setattr(instance, self.param_name, value)

    def validate(self, value):
        for i in value.split():
            if not i[0].isupper() or not i[0].isalpha():
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')



class Student:
    name = NameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.csv_upload(subjects_file)
        self.sub_dic = []

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        else:
            if 2 <= grade <= 5:
                self.subjects[subject]['grade'].append(grade)
                if subject not in self.sub_dic:
                    self.sub_dic.append(subject)
            else:
                raise ValueError('Оценка должна быть целым числом от 2 до 5')

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        else:
            if 0 <= score <= 100:
                self.subjects[subject]['score'].append(score)
                if subject not in self.sub_dic:
                    self.sub_dic.append(subject)
            else:
                raise ValueError('Результат теста должен быть целым числом от 0 до 100')

    def get_average_test_score(self, subject):
        res = 0.0
        cnt = 0
        for i in self.subjects:
            if i == subject:
                if len(self.subjects[i]) != 0:
                    for y in self.subjects[i]['score']:
                        res += y
                        cnt += 1
        val = res if cnt == 0 else res / cnt
        return val

    def get_average_grade(self):
        res = 0.0
        cnt = 0
        for i in self.subjects:
            if len(self.subjects[i]) != 0:
                for y in self.subjects[i]['grade']:
                    res += y
                    cnt += 1
        val = res if cnt == 0 else res / cnt
        return val

    def csv_upload(self, sub_file):
        s = ''
        sub_dict = {}
        with open(sub_file, 'r', encoding='UTF-8') as csv_f:
            csv_reader = csv.reader(csv_f)
            for i in csv_reader:
                s = ', '.join(i)
            for item in s.split(", "):
                sub_dict[item] = {'grade': [], 'score': []}
        return sub_dict

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.sub_dic)}"


if __name__ == '__main__':
    Student = Student('Иван Иванов', 'subjects.csv')
    Student.add_grade("Математика", 4)
    Student.add_test_score("Математика", 85)

    Student.add_grade("История", 2)
    Student.add_test_score("История", 92)
    average_grade = Student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = Student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    print(Student)



#
# import csv
#
# class Student:
#     """
#     Класс, представляющий студента.
#
#     Атрибуты:
#     - name (str): ФИО студента
#     - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов
#
#     Методы:
#     - __init__(self, name, subjects_file): конструктор класса
#     - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
#     - __getattr__(self, name): получение значения атрибута
#     - __str__(self): возвращает строковое представление студента
#     - load_subjects(self, subjects_file): загрузка предметов из файла CSV
#     - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
#     - get_average_grade(self): возвращает средний балл по всем предметам
#     - add_grade(self, subject, grade): добавление оценки по предмету
#     - add_test_score(self, subject, test_score): добавление результата теста по предмету
#     """
#
#     def __init__(self, name, subjects_file):
#         self.name = name
#         self.subjects = {}
#         self.load_subjects(subjects_file)
#     def __setattr__(self, name, value):
#         if name == 'name':
#             if not value.replace(' ', '').isalpha() or not value.istitle():
#                 raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
#         super().__setattr__(name, value)
#
#
#     def __getattr__(self, name):
#         if name in self.subjects:
#             return self.subjects[name]
#         else:
#             raise AttributeError(f"Предмет {name} не найден")
#
#     def __str__(self):
#         return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"
#
#     def load_subjects(self, subjects_file):
#         with open(subjects_file, 'r') as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 subject = row[0]
#                 if subject not in self.subjects:
#                     self.subjects[subject] = {'grades': [], 'test_scores': []}
#     def add_grade(self, subject, grade):
#         if subject not in self.subjects:
#             self.subjects[subject] = {'grades': [], 'test_scores': []}
#         if not isinstance(grade, int) or grade < 2 or grade > 5:
#             raise ValueError("Оценка должна быть целым числом от 2 до 5")
#         self.subjects[subject]['grades'].append(grade)
#
#     def add_test_score(self, subject, test_score):
#         if subject not in self.subjects:
#             self.subjects[subject] = {'grades': [], 'test_scores': []}
#         if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
#             raise ValueError("Результат теста должен быть целым числом от 0 до 100")
#         self.subjects[subject]['test_scores'].append(test_score)
#
#     def get_average_test_score(self, subject):
#         if subject not in self.subjects:
#             raise ValueError(f"Предмет {subject} не найден")
#         test_scores = self.subjects[subject]['test_scores']
#         if len(test_scores) == 0:
#             return 0
#         return sum(test_scores) / len(test_scores)
#
#     def get_average_grade(self):
#         total_grades = []
#         for subject in self.subjects:
#             grades = self.subjects[subject]['grades']
#             if len(grades) > 0:
#                 total_grades.extend(grades)
#         if len(total_grades) == 0:
#             return 0
#         return sum(total_grades) / len(total_grades)
