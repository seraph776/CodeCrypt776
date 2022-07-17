#!/usr/bin/env python3
"""
project: Pytest
created:2022-1-7
@author:seraph1001100
contact:seraph1001100@gmail.com
"""



def add(x, y=2):
    return x + y


def subtract(x, y=2):
    return x - y


def product(x, y=2):
    return x * y


def divide(x, y=2):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x // y
