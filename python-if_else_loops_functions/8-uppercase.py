#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            x = ord(x) - 32
        else:
            x = ord(x)
        print("{}".format(chr(x)), end="")
    print("")
