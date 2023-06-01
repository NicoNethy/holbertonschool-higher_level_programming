#!/usr/bin/python3
coca = "{}"
for x in range(0, 100):
    if x == 99:
        print(coca.format(x))
    else:
        print("{0:0=2d}".format(x), end=", ")