# coding: utf-8

import random

FROM_N, TO_N = 1, 91


class Ticket:
    def __init__(self):
        self._row1, self._row2, self._row3 = [], [], []
        self._rows = {'row1': self._row1, 'row2': self._row2, 'row3': self._row3}
        self._new_ticket(self._rows)

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
                num = random.randrange(FROM_N, TO_N, 1)
                if not self.is_used(num):
                    row.append(num)
                    i += 1
            row.sort()

    def crossing(self, num):
        row_n = 'row' + str(self.is_used(num))
        row = self._rows[row_n]
        i = row.index(num)
        row[i] = ' -'

    def __str__(self):
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
            if space < lenr - 2:
                row_str += '   ' * (lenr - 1 - space)

            row_str += '\n'
        return row_str


ticket = Ticket()
print(ticket)
