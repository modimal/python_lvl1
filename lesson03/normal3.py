# coding: utf-8


def my_filter(func, args):
    if func is None:
        return [arg for arg in args if arg]

    return [arg for arg in args if func(arg)]


print(my_filter(None, ['a', '', 'd', 'cc', ' ']))
print(my_filter(None, [-1, 0, 1, 0, 0, 1, 0, -1]))
print(my_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14]))
