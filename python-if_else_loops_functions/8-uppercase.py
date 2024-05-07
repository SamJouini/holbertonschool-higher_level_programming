#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for char in str:
        letter = ord(char)
        if letter >= ord('a') and letter <= ord('z'):
            upper += chr(letter - 32)
        elif letter >= ord('A') and letter <= ord('Z'):
            upper += char
        else:
            upper += char
    print("{}".format(upper))
