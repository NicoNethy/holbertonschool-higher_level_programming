#!/usr/bin/python3
bbc = "{}"
for x in range(97, 123):
    if x == 101 or x == 113:
        continue
    print(bbc.format(chr(x)), end="")
