# coding: utf-8

import os
import shutil
from re import search

__copy_dir_index = [0, 0, 1]
__copy_file_index = [0, 0, 1]


def __get_npath(dir_path, filename, file_ext, index, mode):

    # Индекс копий перевожу в строку, в зависимости от мода создаётся
    # новое имя файла/директории.

    str_index = ''.join(str(x) for x in index)
    nfilename = 'dir_%s' % str_index if mode == 'dir' else filename + '_copy%s' % str_index + file_ext
    ndir_path = os.path.join(dir_path, nfilename)

    return ndir_path


def make_dir(dir_path):

    # Получаю путь, где следует создавать директорию

    ndir_path = __get_npath(dir_path, None, None, __copy_dir_index, 'dir')

    while os.path.isdir(ndir_path):

        # Проверяю существование директории, если она существует,
        # то инкременчу индекс копии, пока не будет уникальным.

        if __copy_dir_index[2] == 9:

            if __copy_dir_index[1] == 9:
                __copy_dir_index[0] += 1
                __copy_dir_index[1] = 0
            else:
                __copy_dir_index[1] += 1
            __copy_dir_index[2] = 0
        else:
            __copy_dir_index[2] += 1

        ndir_path = __get_npath(dir_path, None, None, __copy_dir_index, 'dir')

    os.mkdir(ndir_path)
    print('Директория %s создана!' % ndir_path)


def remove_dir(dir_path, dir_normpath):
    ndir_path = os.path.join(dir_path, dir_normpath)
    try:
        shutil.rmtree(ndir_path)
        print('Директория %s удалена!' % ndir_path)
    except FileNotFoundError:
        print('Директория %s не найдена!' % ndir_path)


def files_show(dir_path):
    items = os.listdir(dir_path)
    items.sort()
    print('\nСодержимое текущей папки (%s):' % dir_path)
    print(*items, sep=', ')


def file_copy(dir_path, file_path):

    # Вытаскиваю имя файла и его расширение из пути, и получаю путь,
    # где следует создать новую копию.

    result = search('([^\\/:*?"\'<>|\r\n]+)(\..*)$', file_path)
    filename = result.group(1)
    file_ext = result.group(2)

    file_path_copy = __get_npath(dir_path, filename, file_ext, __copy_file_index, 'file')

    while os.path.exists(file_path_copy):

        # Проверяю существование копии файла, если он существует,
        # то инкременчу индекс копии, пока не будет уникальным.

        if __copy_file_index[2] == 9:

            if __copy_file_index[1] == 9:
                __copy_file_index[0] += 1
                __copy_file_index[1] = 0
            else:
                __copy_file_index[1] += 1
            __copy_file_index[2] = 0
        else:
            __copy_file_index[2] += 1

        file_path_copy = __get_npath(dir_path, filename, file_ext, __copy_file_index, 'file')

    shutil.copyfile(file_path, file_path_copy)
    print('\nФайл %s скопирован!' % file_path)


