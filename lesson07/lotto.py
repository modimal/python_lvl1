# coding: utf-8

import re
import random

FROM, TO, ELEM_NUM, COL_NUM, ROW_LEN = 1, 91, 15, 5, 9
ROW_NUM = ELEM_NUM // COL_NUM
ROW_GAPS = ROW_LEN - COL_NUM


class Ticket:
    def __init__(self):
        self._rows = random.sample(range(FROM, TO), ELEM_NUM)
        self._gaps = []

        temp = []
        for i in range(ROW_NUM):
            temp += self._sort(self._rows[i * COL_NUM:(i + 1) * COL_NUM])

            # Создание списка _gaps с пробелами перед i-тым элементом в _rows
            # 1 пустая клетка == 2 символа + 2 пробела по бокам, ROW_GAPS = число пустых клеток в строке
            gap_count = list(range(1, ROW_GAPS + 1))
            for j in range(COL_NUM):
                # Случайным образом выбираю где должны быть пустые клетки
                will_be_gap = bool(random.getrandbits(1))
                if will_be_gap:
                    # Достаю случайным образом кол.-во пустых клеток из gap_count,
                    # n - место, где должен быть перенос строки,
                    # далее удаляю с конца элементы по след. логике:
                    # если ROW_GAPS = 4, gap_mult = 3, gap_count = [1, 2, 3, 4]
                    # то в строке осталось место только для 1 пустой клетки,
                    # следовательно удаляю последние 3 элемента из gap_count --> gap_count = [1]
                    try:
                        gap_mult = random.choice(gap_count)
                        if j == 0:
                            self._gaps.append('n' + ('   ' * gap_mult))
                        else:
                            self._gaps.append('   ' * gap_mult + ' ')
                        gap_count = gap_count[:len(gap_count) - gap_mult]
                        continue
                    except IndexError:
                        pass
                # Если это первый элемент в строке, то вместо пробела будет перенос,
                # иначе перед каждым элементом будет пробел
                self._gaps.append('n') if j == 0 else self._gaps.append(' ')
                # Если это последний элемент в строке и кол.-во пустых клеток в строке < ROW_GAPS,
                # тогда добавить недостающие пустые клетки в конец строки
                if j == COL_NUM - 1 and gap_count:
                    self._gaps[j] += 's   ' * len(gap_count) + ' '
                    continue

        self._rows = temp
        self._formatted = self._format_ticket()

    @property
    def gaps(self):
        return self._gaps

    @property
    def rows(self):
        return self._rows

    @property
    def formatted(self):
        return self._formatted

    def _sort(self, row):
        if len(row) < 2:
            return row

        point = random.choice(row)
        smaller = [x for x in row if point > x]
        bigger = [x for x in row if point < x]
        equals = [x for x in row if point == x]

        return self._sort(smaller) + equals + self._sort(bigger)

    def _format_ticket(self):
        formatted = ''
        self._gaps[0] = self.gaps[0].replace('n', '')  # Если это самый первый элемент, то переноса быть не должно
        for i, x in enumerate(self.gaps):
            x = x.replace('n', '\n')
            # Склеиваю пустые клетки с цифрами, разбиваю пробелы по s, если есть пустые клетки в конце строки,
            # если цифра < 10, тогда добавляю пробел перед ней для ровного вывода
            parts = x.split('s')
            parts.append('')
            if self.rows[i] > 9:
                formatted += parts[0] + str(self.rows[i]) + parts[1]
            else:
                formatted += parts[0] + ' ' + str(self.rows[i]) + parts[1]
        return formatted

    def __str__(self):
        return self.formatted


class Player:
    def __init__(self, name):
        self._ticket = Ticket()
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def ticket(self):
        return self._ticket

    def _check_num(self, num):
        return num in self.ticket.rows

    def crossing(self, num):
        if not self._check_num(num):
            return False
        fr = self._ticket._formatted.replace
        fr = fr(str(num), ' -') if num // 10 != 0 else fr(' ' + str(num) + ' ', ' - ')
        self._ticket._formatted = fr
        return True

    def __str__(self):
        return '--------------------------\n' \
               + self.ticket.__str__() + \
               '\n--------------------------'


class User(Player):
    def __str__(self):
        return '------- Ваш билет --------\n' \
               + self.ticket.__str__() + \
               '\n--------------------------'


class Bot(Player):
    def __str__(self):
        return '---- Билет компьютера ----\n' \
               + self.ticket.__str__() + \
               '\n--------------------------'


class Lotto:
    def __init__(self, user, bot):
        self._user = user
        self._bot = bot
        self._kegs = list(range(FROM, TO))

    @property
    def user(self):
        return self._user

    @property
    def bot(self):
        return self._bot

    def play(self):
        winner = None
        while winner is None:
            random.shuffle(self._kegs)
            randkeg = self._kegs[len(self._kegs) - 1]
            self._kegs.remove(randkeg)

            print('\n==========================\n\nНовый бочонок: {} (осталось {})\n'.format(randkeg, len(self._kegs)))
            print(self.user, self.bot, sep='\n')

            answer = input('\nЗачеркнуть цифру? (y/n)\n').strip().lower()
            self.bot.crossing(randkeg)

            if answer == 'y':
                if not self.user.crossing(randkeg):
                    print('У Вас нет такой цифры. Победил компьютер.')
                    exit(0)
            elif answer == 'n':
                if self.user.crossing(randkeg):
                    print('У Вас была такая цифра. Победил компьютер.')
                    exit(0)
            else:
                raise ValueError('invalid input: expected y or n.')

            winner = self._whos_winner()
        print(winner)

    def _whos_winner(self):
        ure = re.search('[0-9]+', self.user.ticket.formatted)
        bre = re.search('[0-9]+', self.bot.ticket.formatted)
        bure, bbre = ure is None, bre is None

        if bure:
            return '\nВы победили!'
        elif bbre:
            return '\nПобедил компьютер.'


user = User('Игрок')
bot = Bot('Бот 1')
lotto = Lotto(user, bot)
print('\n{}\n{}'.format(user, bot))
lotto.play()
