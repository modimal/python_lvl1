# coding: utf-8

import os
import mods.dirwork as dirwork

do = {
    'mkdir': dirwork.make_dir,
    'rmdir': dirwork.remove_dir,
    'showfiles': dirwork.files_show,
    'copyfile': dirwork.file_copy,
    'q': 'quit'
}

answer = ''
while answer != 'q':
    answer = input('\nсоздать директории в текущей -> mkdir,N\n'
                   'создать директорию в текущей -> mkdir\n'
                   'удалить директорию в текущей (вместо / используйте ,) -> rmdir,dir_normpath\n'
                   'показать всё в текущей директории -> showfiles\n'
                   'скопировать текущий файл (скрипт) -> copyfile\n'
                   'выйти -> q\n').replace(' ', '')
    try:
        answer = answer.split(',')

        if answer[0] == 'mkdir' and len(answer) == 2:
            N = int(answer[1])
            for _ in range(N):
                do[answer[0]](os.getcwd())

        elif answer[0] == 'mkdir':
            do[answer[0]](os.getcwd())

        elif answer[0] == 'rmdir':
            i = 1
            dir_normpath = ''

            while i < len(answer):
                dir_normpath = os.path.join(dir_normpath, answer[i])
                i += 1

            do[answer[0]](os.getcwd(), dir_normpath)

        elif answer[0] == 'showfiles':
            do[answer[0]](os.getcwd())

        elif answer[0] == 'copyfile':
            do[answer[0]](os.getcwd(), os.path.abspath(__file__))

        elif answer[0] == 'q':
            print('\nСпасибо Вам! До свидания!')
            exit(0)

        else:
            print('\nВыбирайте существующие команды!')

    except TypeError as e:
        print('\nНекорректный тип объекта!\n%s' % e)
