#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """A function that reads a text file"""

    with open(filename, "r") as x:
        for i in x.readlines():
            print("{}".format(i), end="")
