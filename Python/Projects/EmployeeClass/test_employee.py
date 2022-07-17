#!/usr/bin/env python3
"""
project: UnitTest
created:2022-1-7
@author:seraph1001100
contact:seraph1001100@gmail.com
"""


import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')
        
    @classmethod
    def teardownClass(cls):
        print('teardownClass')

 
    def setUp(self):
        """Create an instance of an Object"""
        print('setUp')
        self.e1 = Employee('john', 'blackwell', 50000)
        self.e2 = Employee('amy', 'williams', 60000)

  
    def tearDown(self):
        print('tearDown\n')
    

    def test_email(self):
        print('test_email')

        self.e1.first = 'amy'
        self.e2.first = 'john'
        
        self.assertEqual(self.e1.email, 'amy.blackwell@email.com')
        self.assertEqual(self.e2.email, 'john.williams@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.e1.fullname, 'John Blackwell')
        self.assertEqual(self.e2.fullname, 'Amy Williams')
        
        self.e1.first = 'amy'
        self.e2.first = 'john'

        self.assertEqual(self.e1.fullname, 'Amy Blackwell')
        self.assertEqual(self.e2.fullname, 'John Williams')


    def test_apply_raise(self):
        print('test_apply_raise')
        self.e1.apply_raise()
        self.e2.apply_raise()

        self.assertEqual(self.e1.pay, 52500)
        self.assertEqual(self.e2.pay, 63000)

       
if __name__ == '__main__':
    unittest.main()
