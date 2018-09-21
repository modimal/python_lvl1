# coding: utf-8

import os
import shutil

CPDIR_I = 1
CPFILE_I = 1
DIR_HAS_BEEN_CHANGED = False


def __get_npath(dir_path, file_name, file_ext, mode):

    # Создать уникальное имя файла/директории

    nfile_name = 'dir%d' % CPDIR_I if mode == 'dir' else file_name + '_copy%d' % CPFILE_I + file_ext
    npath = os.path.join(dir_path, nfile_name)

    return npath


def make_dir(dir_path):
    global CPDIR_I
    global DIR_HAS_BEEN_CHANGED

    if DIR_HAS_BEEN_CHANGED:
        CPDIR_I = 1
        DIR_HAS_BEEN_CHANGED = False

    # Получить новый абсолютный путь к новой директории

    npath = __get_npath(dir_path, None, None, 'dir')

    # Создание уникального абсолютного пути к новой директории

    while os.path.isdir(npath):
        CPDIR_I += 1
        npath = __get_npath(dir_path, None, None, 'dir')

    os.mkdir(npath)
    print('\nПапка %s успешно создана.' % npath)


def remove_dir(rmpath):
    try:
        shutil.rmtree(rmpath)
        print('\nПапка %s успешно удалена.' % rmpath)
    except FileNotFoundError:
        print('\nОшибка: папка %s не найдена.' % rmpath)
    except NotADirectoryError:
        print('\nОшибка: файл %s не является директорией.' % rmpath)


def show_dir(dir_path):
    try:
        allfiles = os.listdir(dir_path)
        allfiles.sort()
        print('\nВсё, что есть внутри текущей директории (%s):' % dir_path)
        print(*allfiles, sep=', ')
    except FileNotFoundError:
        print('\nОшибка: Папки %s не существует.' % dir_path)


def copyfile(dir_path, file_path):
    global CPFILE_I
    global DIR_HAS_BEEN_CHANGED

    if DIR_HAS_BEEN_CHANGED:
        CPFILE_I = 1
        DIR_HAS_BEEN_CHANGED = False

    # Достаю имя файла и его расширение

    file_info = os.path.splitext(os.path.basename(file_path))
    npath = __get_npath(dir_path, file_info[0], file_info[1], 'file')

    # Создание уникального абсолютного пути к новому файлу-копии

    while os.path.exists(npath):
        CPFILE_I += 1
        npath = __get_npath(dir_path, file_info[0], file_info[1], 'file')

    shutil.copy(file_path, npath)
    print('\nФайл %s успешно скопирован.' % file_path)


def change_dir(dir_path):
    global DIR_HAS_BEEN_CHANGED

    DIR_HAS_BEEN_CHANGED = True
    os.chdir(dir_path)
