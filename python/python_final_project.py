import csv
import logging

"""
    Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
    Также реализуйте возможность запуска из командной строки с передачей параметров.
    Добавить логирования ошибок и логирования полезной информации
"""


class NameValidator:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
        self.log = owner.logger

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        for i in value.split():
            if not i[0].isupper() or not i[0].isalpha():
                self.log.error(f'ФИО должно состоять только из букв {value} и начинаться с заглавной буквы')
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')


class Student:
    logging.basicConfig(filename='python/Log/log_10.log',
                        filemode='w',
                        encoding='utf-8',
                        format='{levelname} - {asctime} функция "{funcName}()"'
                               ' строка {lineno} : {msg}',
                        style='{',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    name = NameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = self.csv_upload(subjects_file)
        self.sub_dic = []

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.logger.error(f'Предмет {subject} не найден')
            raise ValueError(f'Предмет {subject} не найден')
        else:
            if 2 <= grade <= 5:
                self.subjects[subject]['grade'].append(grade)
                if subject not in self.sub_dic:
                    self.sub_dic.append(subject)
            else:
                self.logger.error(f'Оценка {grade} должна быть целым числом от 2 до 5')
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
                self.logger.error(f'Результат теста {score} должен быть целым числом от 0 до 100')
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
        self.logger.info(f'Расчет среднего результата теста {val} выполнен')
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
        self.logger.info(f'Расчет средней оценки {val} выполнен')
        return val

    def csv_upload(self, sub_file):
        s = ''
        sub_dict = {}
        with open('python/' + sub_file, 'r', encoding='UTF-8') as csv_f:
            csv_reader = csv.reader(csv_f)
            for i in csv_reader:
                s = ', '.join(i)
            for item in s.split(", "):
                sub_dict[item] = {'grade': [], 'score': []}
            self.logger.info(f'Предметы из файла {sub_file} загружены')
        return sub_dict

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.sub_dic)}"


def start_(fio, fl, sbj, gr, scr):
    student = Student(fio, fl)
    student.add_grade(sbj, gr)
    student.add_test_score(sbj, scr)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score(sbj)
    print(f"Средний результат по тестам {sbj}: {average_test_score}")
    print(student)
