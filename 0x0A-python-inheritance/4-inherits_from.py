#!/usr/bin/python3
"""Check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of a class that
    inherited from specified class"""
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
