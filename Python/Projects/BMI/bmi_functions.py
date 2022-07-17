#!/usr/bin/env python3
"""created:1/29/2022, author:seraph★776, email: seraph776@gmail.com
PROJECT:: BMI Calculator FUNCTIONS::
This file contains all the BMI functions.
 """

import sys


def get_metrics() -> str:
    """Aks user if they want to calculate BMI for kilograms, pounds, or quit! Also performs input validation
    before returning the metric"""
    while True:
        metric = ''
        user_height = input("Enter (k)ilo, (l)lbs, or (q)uit:\n> ")
        if user_height not in 'klq':
            print("Invalid input! Enter either ('k', 'l', or 'q'):", file=sys.stderr)
            continue
        else:
            break
    if user_height == 'k':
        metric = 'kilograms'
    elif user_height == 'l':
        metric = 'pounds'
    else:
        print('Goodbye!')
        sys.exit()
    return metric


def get_weight(metric: str) -> float:
    """Asks for and returns user's weight Performs input validation before returning user_weight
    Args:
        metric (str):  This will either be 'pounds' or 'kilograms' based on user_input
    Returns:
        user_height (float): The user's weight in either pounds or kilograms determined by user_input
    """
    while True:
        user_weight = input(f'Enter your weight in {metric}:\n> ')
        try:
            user_weight = float(user_weight)
        except ValueError as FOOBAR:
            print('Enter a valid number!', file=sys.stderr)
        break
    return user_weight


def get_height(metric: str) -> float:
    """Asks for and returns user's height Performs input validation before returning user_height
    Args:
        metric (str):  This will either be 'pounds' or 'kilograms' based on user_input
    Returns:
        user_height (float): The user's height in either inches or meters determined by user_input
    """
    d = {'pounds': 'inches', 'kilograms': 'meters'}
    while True:
        user_height = input(f'Enter your height in {d.get(metric, "Invalid entry!")}:\n> ')
        try:
            user_height = float(user_height)
        except ValueError as FOOBAR:
            print('Enter a valid number!', file=sys.stderr)

        break
    return user_height


def calculate_bmi(height: float, weight: float, metric: str) -> float:
    """Calculate and returns user's BMI based on either kilograms or pounds.
    Args:
        height (float): The height of user
        weight (float): The weight of user
        metric (str): This will either be kilograms or pounds based on user_input
    Returns:
        bmi: (float): The user's calculated BMI
    """
    if metric == 'kilograms':
        # If the metrics is in kilograms then perform BMI for kilograms:
        bmi = weight / pow(height, 2)
    else:
        # If the metrics is in pounds then perform BMI for pounds
        bmi = weight / pow(height, 2) * 703
    return bmi


def display_results(bmi) -> str:
    """
    Displays the BMI results!!
    calculation obtained from: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#InterpretedAdults
    """
    bmi_results = f'Your BMI is {bmi:.2f} which falls within the '
    if bmi < 18.5:
        bmi_results += 'underweight range.'
    elif 18.5 <= bmi < 24.9:
        bmi_results += 'normal or Healthy Weight range.'
    elif 25.0 <= bmi < 29.9:
        bmi_results += 'overweight range.'
    elif bmi >= 30.0:
        bmi_results += 'overweight range.'
    return bmi_results + '\n'
