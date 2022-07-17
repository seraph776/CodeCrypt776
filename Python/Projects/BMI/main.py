#!/usr/bin/env python3
"""
created:1/30/2022, author:seraph★776, email: seraph776@gmail.com
PROJECT:BMI CALCULATOR
"""

import unittest
from unittest import mock
from bmi_functions import get_metrics, get_height, get_weight, calculate_bmi, display_results


def main():
    while True:
        # Ask if user wants to use kilograms or pounds
        user_metrics = get_metrics()

        # Ask user for weight in selected metrics
        user_weight = get_weight(metric=user_metrics)

        # Ask user for height in selected metrics
        user_height = get_height(metric=user_metrics)

        # Calculate BMI results based on user_input:
        user_bmi = calculate_bmi(height=user_height, weight=user_weight, metric=user_metrics)

        # Display results:
        print(display_results(bmi=user_bmi))


class TestBMICalculator(unittest.TestCase):
    """Tests BMI functions"""

    def test_get_metric_input_function(self):
        with mock.patch('builtins.input', return_value='k'):
            assert get_metrics() == 'kilograms'

        with mock.patch('builtins.input', return_value='l'):
            assert get_metrics() == 'pounds'

    def test_get_height_function(self):
        with mock.patch('builtins.input', return_value='111.776'):
            assert get_height(metric='pounds') == 111.776

        with mock.patch('builtins.input', return_value='.5000'):
            assert get_height(metric='pounds') == 0.5

        with mock.patch('builtins.input', return_value='0001.5'):
            assert get_height(metric='pounds') == 1.5

        with mock.patch('builtins.input', return_value='7'):
            assert get_height(metric='pounds') == 7.0

    def test_get_weight_function(self):
        with mock.patch('builtins.input', return_value='285'):
            assert get_weight(metric='pounds') == 285.0

        with mock.patch('builtins.input', return_value='7.5000'):
            assert get_weight(metric='pounds') == 7.5

        with mock.patch('builtins.input', return_value='0003.3'):
            assert get_weight(metric='pounds') == 3.3


if __name__ == '__main__':
    unittest.main()
