# coding: utf-8

import re

# Задача 1


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


equation = input("Введите уравнение (y = kx + b): ").replace(" ", "")
x = input("Введите координату точки x: ").replace(" ", "")

k = re.search("=(.*)x", equation)
b = re.search("\+(.*)", equation)

k = k.group(1)
b = b.group(1)

if not is_float(x) or not is_float(k) or not is_float(b) or equation.count("x") > 1:
    print("Ошибка ввода!")
else:
    x = float(x)
    k = float(k)
    b = float(b)
    y = k * x + b
    print("y =", y)

# Задача 2


def are_int(num1, num2, num3):
    try:
        int(num1)
        int(num2)
        int(num3)
        return True
    except ValueError:
        return False


print("\nЗадача 2")

days31 = [1, 3, 5, 7, 8, 10, 12]

date = input("Введите дату в формате dd.mm.yyyy: ").replace(" ", "").split(".")

if len(date) != 3 or not are_int(date[0], date[1], date[2]) or len(date[0]) != 2 or len(date[1]) != 2 or len(date[2]) != 4:
    print("Неправильный формат!")
else:
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    if not 1 <= day <= 31 or not 1 <= month <= 12 or not 1 <= year <= 9999:
        print("Неправильный формат!")
    else:
        if month not in days31 and day == 31:
            print("Неправильное число месяца!")
        else:
            print("Все правильно!")
