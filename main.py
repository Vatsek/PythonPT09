# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

from typing import Callable
import math
import random as rnd
import csv
import json
import os

min_num = -100
max_num = 100


def write_csv_rnd_num(count: int):
    with open('numbers.csv', 'w', encoding='utf-8') as file:
        csv_write = csv.writer(file, dialect='excel', delimiter=',', quoting=csv.QUOTE_ALL)
        all_data = [['A', 'B', 'C']]
        for _ in range(count):
            numbers = []
            for _ in range(len(all_data[0])):
                numbers.append(rnd.randint(min_num, max_num))
            all_data.append(numbers)
        csv_write.writerows(all_data)


def csv_result(func: Callable):
    write_csv_rnd_num(100)

    def wrapper():
        result = {}
        with open('numbers.csv', 'r', encoding='utf-8') as file:
            next(file)
            numbers = list(csv.reader(file))
            count = 1
            for num in numbers:
                num = list(map(int, num))
                if num[0] != 0:
                    res = func(*num)
                    value = {'A': num[0], 'B': num[1], 'C': num[2], 'res': res}
                    result.setdefault(count, value)
                count += 1
        return result
    return wrapper


def json_result(func: Callable):
    count = 1
    result = {}
    if os.path.exists('numbers.csv.json'):
        with open('solutions.json', 'r', encoding='UTF-8') as file:
            result = json.load(file, ensure_ascii=False)

    def wrapper(*args):
        nonlocal count
        res = {'A': args[0], 'B': args[1], 'C': args[2], 'result': func(*args)}
        result.setdefault(count, res)
        count += 1
        with open('numbers.json', 'w', encoding='utf-8') as file_json:
            json.dump(result, file_json, indent=4, ensure_ascii=False)
    return wrapper


@csv_result
@json_result
def quadratic_equation(*args):
    a, b, c, *_ = args
    d = b**2 - 4 * a * c
    if d < 0:
        return None or 'решений нет'
    elif d == 0:
        return -b // (2 * a)
    else:
        return (-b - math.sqrt(d)) // (2 * a), (-b + math.sqrt(d)) // (2 * a)


quadratic_equation()
