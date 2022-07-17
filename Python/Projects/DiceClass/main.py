#!/usr/bin/env python3
"""
project: CodeGuppy
created:2022-1-4
@author:seraph1001100
contact:seraph1001100@gmail.com
"""


from random import randint


class Dice:
    
    def __init__(self, numberOfSides=6):
        self.__numberOfSides = numberOfSides
        self.value = 1

    def throw(self):
        value = randint(1, self.__numberOfSides)
        return value



d1 = Dice()
print(d1.throw())
print(d1.__numberOfSides)  # Returns an traceback error.
