#!/usr/bin/env python3
"""
project: Testing Code
created:2022-1-7
@author:seraph1001100
contact:seraph1001100@gmail.com
"""

import sys
import pytest
import calculator


@pytest.mark.skipif(sys.version_info < (3, 3), reason="Do not run add test")
def test_add():
    assert calculator.add(7, 3) == 10
    assert calculator.add(7) == 9
    assert calculator.add(5) == 7


def test_subtract():
    assert calculator.subtract(8, 3) == 5
    assert calculator.subtract(10) == 8
    assert calculator.subtract(1, 7) == -6


def test_product():
    assert calculator.product(5, 5) == 25
    assert calculator.product(5) == 10
    assert calculator.product(7) == 14


def test_divide():
    assert calculator.divide(8, 2) == 4
    assert calculator.divide(30, 6) == 5
    assert calculator.divide(10) == 5


def test_add_string():
    result = calculator.add("Jon ", "Blackwell") 
    assert result == "Jon Blackwell"


# To test the same function with different values:
@pytest.mark.parametrize('x, y , result',
                          [
                              (7, 3, 10),
                              ('Hello ', 'World!', 'Hello World!'),
                               (10.5, 10.5, 21),
                              ])
def test_add(x, y, result):
    assert calculator.add(x, y) == result
