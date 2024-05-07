#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_argv = len(argv) - 1
    total = 0

for arg in argv[1:]:
        total += int(arg)
        print(total)
