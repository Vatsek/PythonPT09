import math
import random as rnd
import csv


def quadratic_equation(a: int, b: int, c: int):
    d = b**2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b // (2 * a)
    else:
        return (-b - math.sqrt(d)) // (2 * a), (-b + math.sqrt(d)) // (2 * a)


def write_csv_rnd_num(count: int):
    with open('numbers.csv', 'w', encoding='utf-8') as file:
        csv_write = csv.writer(file, dialect='excel', delimiter=',',
                               quoting=csv.QUOTE_ALL)
        all_data = [['A', 'B', 'C']]
        for _ in range(count):
            numbers = []
            for _ in range(3):
                numbers.append(rnd.randint(1, 100))
            all_data.append(numbers)
        csv_write.writerows(all_data)


write_csv_rnd_num(100)
