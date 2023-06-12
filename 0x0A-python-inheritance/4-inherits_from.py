#!/usr/bin/python3
"""Check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of a class that
    inherited from specified class"""
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is not a_class:
            return True
    else:
        return False
