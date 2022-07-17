#!/usr/bin/env python3
"""
project: UnitTest
created:2022-1-7
@author:seraph1001100
contact:seraph1001100@gmail.com
"""


class Employee:
    
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}".title()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

