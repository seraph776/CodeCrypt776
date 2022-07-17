#!/usr/bin/env python3
"""
project: UnitTest
created:2022-1-7
@author:seraph1001100
contact:seraph1001100@gmail.com
"""

import unittest
import calculator


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5 ), 15)
        self.assertEqual(calculator.add(-1, 1 ), 0)
        self.assertEqual(calculator.add(-1, -1 ), -2)
        

    def test_subtract(self):
        self.assertEqual(calculator.subtract(8, 5 ), 3)
        self.assertEqual(calculator.subtract(-2, 2 ), -4)
        self.assertEqual(calculator.subtract(-3, -3 ), 0)


    def test_product(self):
        self.assertEqual(calculator.product(1, 8 ), 8)
        self.assertEqual(calculator.product(-2, 10 ), -20)
        self.assertEqual(calculator.product(-6, -3 ), 18)


    def test_divide(self):
        self.assertEqual(calculator.divide(25, 5 ), 5)
        self.assertEqual(calculator.divide(-1, 1 ), -1)
        self.assertEqual(calculator.divide(-1, -1 ), 1)

        ### Writing test for Exception

        #self.assertRaises(ValueError, calculator.divide, 10, 0)

        ### With context manager - much better
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

        


        
    
    #def test_add(self):
        #result = add(5, 7)
        #self.assertEqual(result, 12)


##    def test_subtract(x, y=2):
##        return x - y
##
##
##    def test_product(x, y=2):
##        return x * y
##
##
##    def test_divide(x, y=2):
##        return x // y
##
##

if __name__ == '__main__':
    unittest.main()
        

    
