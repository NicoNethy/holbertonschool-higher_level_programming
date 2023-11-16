#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """A function that reads a text file"""

    with open(filename, encoding="utf-8") as archivio:
        read_data = archivio.read()
        print(read_data, end='')