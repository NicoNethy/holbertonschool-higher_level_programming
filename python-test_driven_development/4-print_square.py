#!/usr/bin/python3
def text_indentation(text):
    if text == "":
        return
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = ''
    for i in text:
        if i != ' ' and (x != '.' and x != '?' and x != ':'):
            print(x, end="")
        elif i == ' ':
            print(x, end="")
        else:
            print("{}\n".format(x))
        x = i
    print(i, end="")
