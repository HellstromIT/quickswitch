#!/usr/bin/env python

from app.common.walk import walklevel

walk_dirs = ['/home/martin/git', '/home/martin/git/discovery']
found_dirs = []

for directory in walk_dirs:
    found_dirs.append(walklevel(directory))

for directories in found_dirs:
    for directory in directories:
        print(directory[0])
