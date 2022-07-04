#!/usr/bin/python3

"""Return True if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """implementation
    Args:
        obj (Any): object to check
        a_class (type): type to check against

    Returns:
        [boolean]: response
    """
    return type(obj) == a_class
