# coding: utf-8


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def lucky_ticket(ticket_number):
    ticket_number = list(ticket_number)
    ticket_length = len(ticket_number)
    sum_1st = 0
    sum_2nd = 0

    i = 0
    while i < ticket_length:
        if i < ticket_length / 2:
            sum_1st += int(ticket_number[i])
        else:
            sum_2nd += int(ticket_number[i])
        i += 1

    # Если в билете нечетное кол-во чисел, то добавить число посередине во 2-ую сумму
    sum_2nd = sum_2nd + int(ticket_number[ticket_length // 2]) if ticket_length % 2 != 0 else sum_2nd

    return True if sum_1st == sum_2nd else False


user_ticket = input("Введите номер вашего билета: ").strip()

if not is_int(user_ticket):
    print("Введите корректный номер билета!")
else:
    if lucky_ticket(user_ticket):
        print("У вас счастливый билет!")
    else:
        print("Ничего! Повезет в следующий раз!")
