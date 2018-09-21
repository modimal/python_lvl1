# coding: utf-8

import random

origin_list = [random.randrange(-100, 100, 1) for _ in range(15)]
new_list = [x for x in origin_list if x % 3 == 0 and x > 0 and x % 4 != 0]

print("Исходный список: {}\nНовый список: {}".format(origin_list, new_list))
