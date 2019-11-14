#!/usr/bin/env python3

from app.common.walk import walklevel
from pathlib import Path

home = str(Path.home())

walk_dirs = [home + '/git', home + '/git/discovery']
found_dirs = []

for directory in walk_dirs:
    found_dirs.append(walklevel(directory))

for directories in found_dirs:
    for directory in directories:
        print(directory[0])
