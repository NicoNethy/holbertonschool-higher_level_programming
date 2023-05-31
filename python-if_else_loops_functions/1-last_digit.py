#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number *= -1
    div = number % 10
    number *= -1
    div *= -1
else:
    div = number % 10
print("Last digit of " + (f"{number}") + " is " + (f"{div}"))
