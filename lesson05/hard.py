# coding: utf-8
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil

CPFILE_INDEX = 0

print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки\n'
          'mkdir <dir_name> - создание директории\n'
          'cp <file_name> - создание копии указанного файла\n'
          'rm <file_name> - удаление указанного файла\n'
          'cd <full_path or relative_path> - изменение текущей директории на указанную\n'
          'ls - отображение полного пути текущей директории\n'
          'ping - тестовый ключ')


def make_dir():
    dir_name = file_name

    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return

    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print('pong')


def cpfile_index_increment():
    global CPFILE_INDEX
    cpstart, cpi = 1, 1

    CPFILE_INDEX = cpstart if CPFILE_INDEX == 0 else CPFILE_INDEX + cpi

    return str(CPFILE_INDEX).zfill(3)


def copy_file():
    global file_name

    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return

    file_path = os.path.abspath(file_name)
    cpfull = file_name
    cpname, cpext = os.path.splitext(file_name)

    while os.path.isfile(cpfull):
        tmp_cpname = cpname + '_copy{}'.format(cpfile_index_increment())
        cpfull = tmp_cpname + cpext

    try:
        shutil.copy(file_path, os.path.abspath(cpfull))
        print('Файл {} скопирован'.format(file_path))
    except FileNotFoundError:
        print('Файла {} не существует'.format(file_path))
    except PermissionError as e:
        print('Отказано в доступе:\n{}'.format(e))


def remove_file():
    global file_name

    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return

    file_path = os.path.abspath(file_name)
    answer = input('Вы уверены, что хотите удалить файл (y/n):\n{}\n'.format(file_path)).strip().lower()

    if answer == 'y':
        try:
            os.remove(file_path)
            print('Файл {} удален'.format(file_path))
        except FileNotFoundError:
            print('Файла {} не существует'.format(file_path))
        except PermissionError as e:
            print('Отказано в доступе:\n{}'.format(e))


def change_dir():
    dir_name = file_name
    dir_path = os.path.abspath(dir_name)
    try:
        os.chdir(dir_path)
        print('Ваша текущая директория: {}'.format(dir_path))
    except FileNotFoundError:
        print('Директории {} не существует'.format(dir_path))


def get_dir_fullpath():
    print('Полный путь текущей директории:\n{}'.format(os.path.abspath(os.getcwd())))


do = {
    'help': print_help,
    'mkdir': make_dir,
    'cp': copy_file,
    'rm': remove_file,
    'cd': change_dir,
    'ls': get_dir_fullpath,
    'ping': ping
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')
