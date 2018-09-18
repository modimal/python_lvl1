# coding: utf-8

import os
import random

path = os.path.join('..', 'files', 'normal3.txt')

with open(path, 'w', encoding='UTF-8') as f:
    for _ in range(2500):
        f.write(str(random.randrange(0, 10, 1)))

with open(path, 'r', encoding='UTF-8') as f:
    print(len(f.readline()))
