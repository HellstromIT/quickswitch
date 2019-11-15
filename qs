#!/usr/bin/env python3

from app.common.walk import walklevel
from app.common.helpers import addDirectory, listDirectories
from app.data.config import Configuration
import argparse
from argparse import RawTextHelpFormatter


config = Configuration()


def addDirectory(folder):
    config.addFolder(folder)
    config.writeConfig()


def listDirectories():
    for directory in config.getDirectories():
        for dirs in walklevel(directory):
            print(dirs[0])


def main():
    parser = argparse.ArgumentParser(description='Get directories from within a set of directories')
    parser.add_argument("--add", help="Add directory to be searched")
    args = parser.parse_args()
    if args.add:
       addDirectory(args.add)
    else:
       listDirectories()


if __name__ == '__main__':
    main()
