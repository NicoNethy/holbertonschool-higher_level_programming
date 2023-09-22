#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    coca = add(a, b)
    bbc = "{} + {} = {}"
    print(bbc.format(a, b, coca))
    