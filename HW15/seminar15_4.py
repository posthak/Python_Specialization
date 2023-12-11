"""
Задание No4
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3 - я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.
"""

from datetime import datetime, timedelta
import calendar

"""
Задание №4.
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответствует формату.
"""

import logging
from datetime import datetime, date

logging.basicConfig(filename='HW15/Log/log_4.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} функция "{funcName}()"'
                           ' строка {lineno} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def text_to_date(text):
    months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'июн': 6,
              'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10,
              'ноя': 11, 'дек': 12}
    weekdays = {'пон': 0, 'вто': 1, 'сре': 2, 'чет': 3, 'пят': 4, 'суб': 5,
                'вос': 6}

    '''Перевод текст в дату'''
    try:
        count, weekday_, month_, *other = text.split()  # 3-я среда мая

        count = int(count[0])
        if count > 5:
            raise Exception('некорректная неделя')
        weekday = weekdays[weekday_[:3]]
        m = month_[:3]
        if m == "мая":
            month_ = "май"
        month = months[month_[:3]]  # 5 - число
    except Exception as exc:
        logger.info(
            f'Переданные данные: {count}-й , день недели"{weekday_}",'
            f' месяц:"{month_}" =  ошибочные данные: {exc}')
        count = 0

    if count:
        count_week = 0
        year = datetime.now().year  # 2023
        for day in range(1, 32):
            try:
                result = date(year=year, month=month, day=day)
                if result.weekday() == weekday:
                    count_week += 1
                    if count_week == count:
                        logger.info(
                            f'{count}-й {weekday_} {month_} {year} = {result} ')
                        return result
            except ValueError as e:
                logger.info(
                    f'Переданные данные: {count}-й , день недели"{weekday_}",'
                    f' месяц:"{month_}" =  ошибочные данные: {e}')
                print(f'преобразование невозможно. см. Log/log_4.log')
        print(f'преобразование невозможно')
        logger.info(
            f'Переданные данные: {count}-й , день недели"{weekday_}",'
            f' месяц:"{month_}". Преобразование невозможно')

    else:
        print(f'преобразование невозможно. см. Log/log_4.log')
        return None


if __name__ == '__main__':
    print(text_to_date('3-й вто мая'))
    # print(text_to_date('3-й вторник марта'))
    # print(text_to_date('5-й понедельник сентября'))
    # print(text_to_date('5-й четверг августа'))

#
# def convert_text_to_date(text):
#     parts = text.split()
#     # Словарь для преобразования порядковых номеров в числовые значения
#     ordinal_numbers = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5}
#     try:
#         # получим порядковый номер и день недели из входного текста
#         ordinal = ordinal_numbers[parts[0].lower()]
#         weekday = parts[1].capitalize()
#         month = parts[3].capitalize()
#
#         # получим текущий год
#         current_year = datetime.now().year
#         # найдём индекс дня недели (0-6) используя модуль calendar
#         weekday_index = list(calendar.day_name).index(weekday)
#         # найдём первое появление дня недели в месяце
#         dt = datetime(current_year, datetime.strptime(month, '%B').month, 1)
#
#         while dt.weekday() != weekday_index:
#             dt += timedelta(days=1)
#
#         # прибавляем смещение в днях
#         dt += timedelta(days=(ordinal - 1) * 7)
#         return dt
#     except (ValueError, IndexError, KeyError) as e:
#         print(f'Ошибка: {e}')
#         return None
