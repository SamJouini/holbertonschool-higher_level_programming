#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_argv = len(argv) - 1
    total = 0

if num_argv == 0:
    print("0")
elif num_argv == 1:
    print("1")
else:
    for arg in argv[1:]:
        total += int(arg)
    print(total)
