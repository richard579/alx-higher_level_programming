#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    new_list = [not i % 2 for i in my_list]
    return (new_list)
