# coding=utf-8
from __future__ import unicode_literals, print_function


def parenthetics(string):
    """Check if string is balanced."""
    paren_counter = 0

    for x in string:
        if paren_counter < 0:
            return -1

        elif x == '(':
            paren_counter += 1

        elif x == ')':
            paren_counter -= 1

    return paren_counter
