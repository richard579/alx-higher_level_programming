#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictonary):
        value = a_dictionary.get(key)
        print('{}: {}'.format(key,value))
