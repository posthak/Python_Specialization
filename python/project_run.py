import argparse
from python_final_project import start_

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Принимаем строку с датой")
    parser.add_argument('-fio', type=str, default='Иван Иванов')
    parser.add_argument('-fl', type=str, default='subjects.csv')
    parser.add_argument('-sbj', type=str, default='Математика')
    parser.add_argument('-gr', type=int, default=1)
    parser.add_argument('-scr', type=int, default=91)

    args = parser.parse_args()
    print(args)
    fio = str(args.fio)
    fl = str(args.fl)
    sbj = str(args.sbj)
    gr = int(args.gr)
    scr = int(args.scr)
    start_(fio, fl, sbj, gr, scr)

    # запуск командной строкой:python3 python/project_run.py -fio='Иван Иванов' -fl='subjects.csv' -sbj='Математика' -gr=4 -scr=85
