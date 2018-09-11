# coding: utf-8

import math
import random

# Задача 1

print("\nЗадача 1")


def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


random_list = input("Введите последовательность чисел через запятую: ").replace(" ", "").split(",")
random_list = [int(x) for x in random_list if x != "" and is_int(x)]

new_list = [int(math.sqrt(x)) for x in random_list if x >= 0 and math.sqrt(x).is_integer()]

print(random_list)
print(new_list)

# Задача 2

print("\nЗадача 2")

days = {
    "01": "первое",
    "02": "второе",
    "03": "третье",
    "04": "четвёртое",
    "05": "пятое",
    "06": "шестое",
    "07": "седьмое",
    "08": "восьмое",
    "09": "девятое",
    "10": "десятое",
    "11": "одиннадцатое",
    "12": "двенадцатое",
    "13": "тринадцатое",
    "14": "четырнадцатое",
    "15": "пятнадцатое",
    "16": "шестнадцатое",
    "17": "семнадцатое",
    "18": "восемнадцатое",
    "19": "девятнадцатое",
    "20": "двадцатое",
    "21": "двадцать первое",
    "22": "двадцать второе",
    "23": "двадцать третье",
    "24": "двадцать четвёртое",
    "25": "двадцать пятое",
    "26": "двадцать шестое",
    "27": "двадцать седьмое",
    "28": "двадцать восьмое",
    "29": "двадцать девятое",
    "30": "тридцатое",
    "31": "тридцать первое"
}

months = {
    "01": "января",
    "02": "февраля",
    "03": "марта",
    "04": "апреля",
    "05": "мая",
    "06": "июня",
    "07": "июля",
    "08": "августа",
    "09": "сентября",
    "10": "октября",
    "11": "ноября",
    "12": "декабря"
}

date = input("Введите дату в формате dd.mm.yyyy: ").replace(" ", "")

if len(date) != 10:
    print("Неверный формат ввода!")
else:
    date_format = date.split(".")
    print("{0} {1} {2} года".format(days[date_format[0]], months[date_format[1]], date_format[2]))

# Задача 3

print("\nЗадача 3")

n = int(input("n = "))

random_list = [random.randint(-100, 100) for x in range(n)]
print(random_list)

# Задача 4

print("\nЗадача 4")

random_list = [random.randint(1, 10) for x in range(10)]
print(random_list)
list_a = []
list_b = [x for x in random_list if random_list.count(x) == 1]

for x in random_list:
    if x not in list_a:
        list_a.append(x)

print(list_a)
print(list_b)
