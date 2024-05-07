#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    print(f"{num_args}: argument")
    print(": " if num_args == 0 else ":")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
