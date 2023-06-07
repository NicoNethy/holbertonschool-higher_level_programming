#!/usr/bin/python3
import sys
def print_list_integer(my_list=[]):
    argc = len(my_list) - 1
    if argc > 1:
        for arg in range(len(my_list[0:])):
            print("{}".format(my_list[arg]))


my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)