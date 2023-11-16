#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and
      returns the number of characters written:"""

    with open(filename, 'w', encoding="utf-8") as archivio:
        archivio.write(text)
    return len(text)