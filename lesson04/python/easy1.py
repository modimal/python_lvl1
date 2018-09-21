# coding: utf-8

import random

origin_list = [random.randrange(-15, 15, 1) for _ in range(10)]
sqr_list = [x**2 for x in origin_list]

print("Исходный список: {0}\nСписок с квадратами: {1}".format(origin_list, sqr_list))
