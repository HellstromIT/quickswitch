#!/usr/bin/env python3

from app.common.helpers import addDirectory, selectDirectory
from app.data.config import Configuration
from app import _version
import argparse
from argparse import RawTextHelpFormatter
import os


config = Configuration()


def main():
    parser = argparse.ArgumentParser(description='Get directories from within a set of directories')
    parser.add_argument("--add", help="Add directory to be searched")
    parser.add_argument('-v', '--version', action='version', version="{prog}: {version}".format(prog="QuickSwitch", version=_version.__version__), help="Print quickswitch version")
    args = parser.parse_args()
    cwd = os.getcwd()
    if args.add:
       addDirectory(config, args.add)
    else:
       selectDirectory(config, cwd)


if __name__ == '__main__':
    main()
