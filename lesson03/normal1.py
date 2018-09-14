# coding: utf-8


def fibonacci(n, m):
    fi_row = []
    i = 1
    x = 1
    y = 1
    while i <= m:
        if i >= n:
            fi_row.append(x)

        x, y = y, x + y
        i += 1

    return fi_row


try:
    n = int(input("n = ").strip())
    m = int(input("m = ").strip())
    print(fibonacci(n, m))
except ValueError:
    print("Вводите целые числа больше 1!")
