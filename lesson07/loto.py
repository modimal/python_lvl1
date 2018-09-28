# coding: utf-8

import random

FROM_N, TO_N = 1, 91


class Ticket:
    def __init__(self):
        self._row1, self._row2, self._row3 = [], [], []
        self._rows = {'row1': self._row1, 'row2': self._row2, 'row3': self._row3}
        self._new_ticket(self._rows)
        self._formatted = self._format_ticket()

    @property
    def rows(self):
        return self._rows

    def is_used(self, num):
        if num in self._row1:
            return 1
        elif num in self._row2:
            return 2
        elif num in self._row3:
            return 3
        return 0

    def _new_ticket(self, rows):
        for k, row in rows.items():
            i = 0
            while i < 5:
                num = random.randrange(FROM_N, TO_N)
                if not self.is_used(num):
                    row.append(num)
                    i += 1
            row.sort()

    def crossing(self, num):
        row_n = 'row' + str(self.is_used(num))
        row = self._rows[row_n]
        row.remove(row[row.index(num)])
        num = str(num)
        num = ' ' + num + ' ' if len(num) == 1 else num
        self._formatted = self._formatted.replace(num if len(num) == 3 else num, ' - ')

    def _format_ticket(self):
        row_str = ''
        for k, row in self._rows.items():
            space, i, lenr = 0, 0, len(row)

            while i < lenr:
                if space < lenr - 1 and bool(random.getrandbits(1)):
                    space += 1
                    row_str += '   '
                else:
                    x = str(row[i])
                    row_str += x + ' ' if len(x) == 2 else ' ' + x + ' '
                    i += 1
            if space < lenr - 1:
                row_str += '   ' * (lenr - 1 - space)

            row_str += '\n'
        return row_str

    def __str__(self):
        return self._formatted


class UserTicket(Ticket):
    def __str__(self):
        return '------ Ваша карточка -----\n'\
               + super().__str__() + \
               '--------------------------'


class CompTicket(Ticket):
    def __str__(self):
        return '-- Карточка компьютера ---\n' \
               + super().__str__() + \
               '--------------------------'


user_ticket = UserTicket()
comp_ticket = CompTicket()
kegs = list(range(FROM_N, TO_N))

print('\n{}\n\n{}'.format(user_ticket, comp_ticket))

while True:
    is_user_winner = all(len(v) == 0 for v in user_ticket.rows.values())
    is_comp_winner = all(len(v) == 0 for v in comp_ticket.rows.values())

    if is_user_winner and is_comp_winner:
        print('Ничья!')
        exit(0)
    elif is_user_winner:
        print('Поздравляю! Вы победили!')
        exit(0)
    elif is_comp_winner:
        print('В этот раз выиграл компьютер.')
        exit(0)

    random_keg_i = random.randrange(len(kegs))

    print('\nНовый бочонок: {} (осталось {})\n{}\n\n{}'
          .format(kegs[random_keg_i], len(kegs) - 1, user_ticket, comp_ticket))

    answer = input('Зачеркнуть цифру? (y/n)\n').strip().lower()

    if comp_ticket.is_used(kegs[random_keg_i]):
        comp_ticket.crossing(kegs[random_keg_i])

    if answer == 'y':
        if user_ticket.is_used(kegs[random_keg_i]):
            user_ticket.crossing(kegs[random_keg_i])
        else:
            print('У Вас нет такой цифры. Вы проиграли.')
            exit(0)
    elif answer == 'n':
        if user_ticket.is_used(kegs[random_keg_i]):
            print('У Вас есть такая цифра. Вы проиграли.')
            exit(0)
    else:
        raise ValueError('вводите только допустимые символы (y/n)')

    kegs.remove(kegs[random_keg_i])
