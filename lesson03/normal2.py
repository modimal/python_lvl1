# coding: utf-8

import random


def sort_to_max(origin_list):
    if len(origin_list) <= 1:  # Вернуть список, если он пустой или состоит из 1-го элемента
        return origin_list

    main_num = random.choice(origin_list)  # Выбрать опорный элемент
    smaller_nums = [num for num in origin_list if num < main_num]  # Все числа меньшие опорного
    larger_nums = [num for num in origin_list if num > main_num]  # Все числа больше опорного
    equal_nums = [num for num in origin_list if num == main_num]  # Все числа равные опорному

    # Рекурсивно отсортировать оставшиеся части и вернуть целый список
    return sort_to_max(smaller_nums) + equal_nums + sort_to_max(larger_nums)


num_list = [random.randrange(-100, 100, 1) for x in range(10)]
print(num_list)
print(sort_to_max(num_list))
