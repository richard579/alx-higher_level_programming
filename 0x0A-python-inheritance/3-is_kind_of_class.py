#!/usr/bin/python3
"""Check if object is instance of class or subclass"""


def is_kind_of_class(obj, a_class):
    """Return True is isinstance is true else false"""
    x = isinstance(obj, a_class)
    if x:
        return True
    return False
