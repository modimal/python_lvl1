# coding: utf-8


def sqr_sum(*args):
    summ = 0
    for arg in args:
        summ += arg ** 2

    return summ


print(sqr_sum(3, 4, 5, 6, 7))
