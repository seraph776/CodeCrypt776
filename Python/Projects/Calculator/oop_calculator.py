#!/usr/bin/env python3
"""
created: 2022-06-20 15:40:03
@author: seraph★1001100
contact: admin@gurucodex.com
project: OOP Calculator
metadoc: This program was designed for a Codewars Kata competition 
license: MIT
"""


import sys


class Calculator:
    """Calculator class."""

    OPTIONS = {1: 'addition',
               2: 'subtraction',
               3: 'multiplication',
               4: 'division',
               7: 'quit'}

    def __init__(self, n1=None, n2=None):
        """Initialize attributes"""
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        """Returns the sum of n1 & n2."""
        return self.n1 + self.n2

    def subtraction(self):
        """Returns the difference of n1 & n2."""
        return self.n1 - self.n2

    def multiplication(self):
        """Returns the products of n1 & n2."""
        return self.n1 * self.n2

    def division(self):
        """Returns the quotient of n1 & n2."""
        try:
            return self.n1 / self.n2
        except ZeroDivisionError as e:
            return error_message(f'{chr(128369)} {e}!')


def get_integer_inputs() -> list:
    """Receives two numeric inputs from user, and returns results."""
    # This hashes the iteration to the ordinal number of inputs.
    ht = {1: '1st', 2: '2nd'}
    output = []
    while len(output) != 2:
        while True:
            user_input = input(f'Enter {ht.get(len(output) + 1)} digit:\n{chr(129094)} ')
            if not user_input.isdigit():
                print(error_message('Invalid input!'))
                continue
            else:
                break
        # append user's input to output list.
        output.append(user_input)
    # cast elements in list to integer.
    return [int(i) for i in output]


def display_option_menu(menu_options: dict) -> str:
    """Displays calculator options, and returns user's choice."""
    for k, v in menu_options.items():
        print(f'\t({k})-{v.title()}')

    while True:
        user_input = input(f'Select the digit of the operation (1-{len(menu_options)}):\n{chr(129094)} ')
        # Validate input: If not a digit or in menu option, continue to ask user for input.
        if not user_input.isdigit() or int(user_input) not in menu_options:
            print(error_message('Invalid input!'))
            continue
        else:
            # If input is valid; break.
            break
    # Returns user's choice.
    return menu_options.get(int(user_input))


def highlight_mode(text: str) -> str:
    """teal color font to highlight operation mode, and function output."""
    return f"\033[36m{text}\033[0m"


def error_message(text: str) -> str:
    """red color font to highlight error messages."""
    return f"\033[31m{text}\033[0m"


def main():
    # Initialize calculator instance.
    calc = Calculator()
    # Initialize calculator options.
    calculator_options = Calculator.OPTIONS
    while True:  # Start main loop.
        print(f'-- CALCULATOR OPTIONS --')
        # Display calculator options, and get users input.
        users_input = display_option_menu(calculator_options)
        # (!): This is for aesthetic purposes. An operator sign will appear depending on what the user's selects.
        symbol = {'addition': '+', 'subtraction': '-', 'multiplication': '*', 'division': '÷'}
        # Display the selected calculator option as a header; for orientation.
        print(highlight_mode(f'{symbol.get(users_input)} {users_input.title()} Mode'))
        match users_input:
            case 'quit':
                print('Goodbye!')
                return sys.exit()
        # Assign calc.n1 & calc.n1 integer values.
        calc.n1, calc.n2 = get_integer_inputs()
        match users_input:
            # Perform selected operations:
            case 'addition':
                print(highlight_mode(f'{chr(11035)} TOTAL: {calc.addition()}'))
            case 'subtraction':
                print(highlight_mode(f'{chr(11035)} TOTAL:  {calc.subtraction()}'))
            case 'multiplication':
                print(highlight_mode(f'{chr(11035)} TOTAL: {calc.multiplication()}'))
            case 'division':
                print(highlight_mode(f'{chr(11035)} TOTAL: {calc.division()}'))
            case _:
                return main()


if __name__ == '__main__':
    main()
