# coding=utf-8
from __future__ import unicode_literals, print_function


def test_paren():
    """Test Parenthetics."""
    from parenthetics import parenthetics
    assert parenthetics('()()()') == 0
    assert parenthetics(')()()()(') == -1
    assert parenthetics('()()(') == 1
