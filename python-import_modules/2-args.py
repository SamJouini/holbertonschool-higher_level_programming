#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_argv = len(argv) - 1

    if num_argv == 0:
        print("0 arguments.")
    elif num_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_argv))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
