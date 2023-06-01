#!/usr/bin/python3

def comb3():
    bbc = "{}{}"
    for i in range(0, 10):
        for x in range(i + 1, 10):
            print(bbc.format(i, x), end=", " if i < 8 else "\n")


from 6-print_comb3 import comb3

comb3()