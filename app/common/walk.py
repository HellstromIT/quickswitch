import os

def walklevel(walk_dir, level=1):
    walk_dir = walk_dir.rstrip(os.path.sep)
    assert os.path.isdir(walk_dir)
    num_sep = walk_dir.count(os.path.sep)
    for root, dirs, files in os.walk(walk_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]
