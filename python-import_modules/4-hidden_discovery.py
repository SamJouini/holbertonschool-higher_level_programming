#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for hidden in dir(hidden_4):
        if hidden[0] != "_":
            print(hidden)
