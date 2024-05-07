#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    
    if len_argv == 0:
        print("0 arguments.")
    elif len_argv == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_argv))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, argv[i]))

