#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = number % -10
        x *= -1
    else:
        x = number % 10
    print(x, end="")
    return(x)
