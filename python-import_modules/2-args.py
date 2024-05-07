#!/usr/bin/python3

import sys import argv

if __name__ == "__main__":
    num_argv = len(sys.argv) - 1

    if num_argv == 0:
        print("0 arguments.")
    elif num_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_argv))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, argv[i]))
