# coding: utf-8

import re


def my_round(number, ndigits):
    try:
        if re.search("\.", number) is None:  # Является ли число float
            return number

        ndigits = int(ndigits)
        before_dot = re.search("(.*)\.", number).group(1)  # Нахожу числа до точки
        after_dot = list(re.search("\.(.*)", number).group(1))  # Нахожу числа после точки

        if len(after_dot) + 1 == int(ndigits):  # Нужно ли его округлять
            return number

        detachable_1st = int(after_dot[ndigits - 1])  # Первое отделяемое число

        try:
            detachable_2nd = int(after_dot[ndigits])  # Второе отделяемое число
        except IndexError:
            detachable_2nd = 0

        # Если 1ое отделяемое число больше 5 или, если оно равно 5 и 2ое отделяемое является значимым,
        # тогда усиливаем последнее оставляемое число

        if detachable_1st > 5 or (detachable_1st == 5 and detachable_2nd != 0):

            # Если после округления число останется float
            if ndigits > 1:
                after_dot[ndigits - 2] = str(int(after_dot[ndigits - 2]) + 1)
                after_dot = after_dot[:ndigits - 1]
                after_dot = ''.join(after_dot)
                return before_dot + "." + after_dot

            # Если после округления число станет int
            else:
                before_dot = list(before_dot)
                before_dot[len(before_dot) - 1] = str(int(before_dot[len(before_dot) - 1]) + 1)
                before_dot = ''.join(before_dot)
                return before_dot

        # В другом случае округляем вниз
        else:
            after_dot = after_dot[:ndigits - 1]
            after_dot = ''.join(after_dot)
            before_dot = before_dot + "." + after_dot if after_dot != "" else before_dot
            return before_dot
    except:
        return "Ошибка! Вводите корректные числа!"


user_number = input("Введите число: ").strip()
user_ndigits = input("Введите кол-во знаков (1 знак - 1 число перед запятой): ").strip()

print(my_round(user_number, user_ndigits))
