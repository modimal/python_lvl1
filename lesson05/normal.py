# coding: utf-8

import os
import mods.dirwork as dirwork

do = {
    'mkdir': dirwork.make_dir,
    'rmdir': dirwork.remove_dir,
    'show': dirwork.show_dir,
    'copy': dirwork.copyfile,
    'chdir': dirwork.change_dir
}

answer = ''

while True:
    answer = input('\nСоздать новую папку в текущей -> mkdir\n'
                   'Создать несколько новых папок в текущей -> mkdir,N\n'
                   'Удалить папку -> rmdir,относительный_путь\n'
                   'Показать всё в текущей папке -> show\n'
                   'Копировать текущий скрипт -> copy\n'
                   'Перейти в папку -> chdir,относительный_путь\n'
                   'Завершить сеанс -> exit\n').replace(' ', '').split(',')

    if answer[0] == 'mkdir' and len(answer) == 2:
        try:
            N = int(answer[1])
            N = None if N < 1 else N

            for _ in range(N):
                do[answer[0]](os.getcwd())

        except (ValueError, TypeError):
            print('\nОшибка: mkdir,N -> вводите целое число N больше 0!')

    elif answer[0] == 'mkdir':
        do[answer[0]](os.getcwd())

    elif answer[0] == 'rmdir':
        rmpath = os.path.abspath(answer[1])
        do[answer[0]](rmpath)

    elif answer[0] == 'show':
        do[answer[0]](os.getcwd())

    elif answer[0] == 'copy':
        do[answer[0]](os.getcwd(), os.path.abspath(__file__))

    elif answer[0] == 'chdir':
        do[answer[0]](os.path.abspath(answer[1]))

    elif answer[0] == 'exit':
        exit(0)

    else:
        print('\nВводите существующие команды.')




