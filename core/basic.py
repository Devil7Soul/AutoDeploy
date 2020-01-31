#!/usr/bin/env python3
# Author : Kevin
# Time   : 31/01/2020 6:44 PM
# File   : basic.py.py
# IDE    : PyCharm

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('dir', BASE_DIR)

f = open(BASE_DIR+'/conf/settings.conf', 'r', encoding='utf-8')
for i in f:
    # if i[0] == '#':
    #     continue
    if i.startswith('#', 0):
        continue
    print(i)
f.close()