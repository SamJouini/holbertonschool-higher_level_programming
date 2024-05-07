#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    print(f"{'s' if num_args != 1 else ''} argument: {num_args}")
    print(": " if num_args == 0 else ":")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
