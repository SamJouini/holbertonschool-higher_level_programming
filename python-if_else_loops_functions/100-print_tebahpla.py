#!/usr/bin/python3

print(''.join(chr(char) for char in range(122, 64, -1) for case in (lambda x: x, lambda x: x-32) if chr(case(char)).isalnum()), end='')
