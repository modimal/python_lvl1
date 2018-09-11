# coding: utf-8

import random

# Задача 1

print("\nЗадача 1")

user_list = input("Введите значения списка через запятую: ").replace(" ", "").split(",")
user_list = [x for x in user_list if x != ""]

for i, item in enumerate(user_list):
    print("{0}. {1}".format(i + 1, item))

# Задача 2

print("\nЗадача 2")

list1 = [random.randrange(1, 11, 1) for x in range(5)]
list2 = [random.randrange(5, 16, 1) for x in range(5)]

print("\nПервый список:", list1)
print("Второй список:", list2)

tmp_list = [x for x in list1 if x not in list2]
list1 = tmp_list

print("Первый список с изменениями:", list1)

# Задача 3

print("\nЗадача 3")

random_list = [random.randrange(5, 26, 1) for x in range(10)]
new_list = [int(x / 4) if x % 2 == 0 and (x / 4).is_integer() else x / 4 if x % 2 == 0 else x * 2 for x in random_list]

print("Исходный список:", random_list)
print("Новый список:", new_list)
