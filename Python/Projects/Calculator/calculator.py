#!/usr/bin/env python3
"""
created: 2022-06-18 22:24:14
@author: seraph★1001100
contact: admin@codecrypt76.com
project: 
metadoc: 
license: None
"""

import sys


class Calculator:
    """A calculator class"""

    def __init__(self, n1=None, n2=None):
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        """Returns the sum of n1 & n2"""
        self.n1, self.n2 = get_numeric_input()
        return self.n1 + self.n2

    def subtraction(self):
        """Returns the difference of n1 & n2"""
        self.n1, self.n2 = get_numeric_input()
        return self.n1 - self.n2

    def multiplication(self):
        """Returns the products of n1 & n2"""
        self.n1, self.n2 = get_numeric_input()
        return self.n1 * self.n2

    def division(self):
        """Returns the quotient of n1 & n2"""
        self.n1, self.n2 = get_numeric_input()
        try:
            return self.n1 / self.n2
        except ZeroDivisionError as e:
            return f'🕱 {e}'

    def modulus(self):
        """Returns the quotient remainder of n1 & n2"""
        self.n1, self.n2 = get_numeric_input()
        return self.n1 % self.n2

    def exponents(self):
        """Returns n1 raised to the power of n2"""
        self.n1, self.n2 = get_numeric_input()
        return self.n1 ** self.n2


def get_display_options() -> str:
    """Displays available calculator options, and returns user's choice"""
    options = {1: 'addition',
               2: 'subtraction',
               3: 'multiplication',
               4: 'division',
               5: 'modulus',
               6: 'exponent',
               7: 'quit'}
    print(f'Instructions: Select a digit of an operation to be performed (1-{len(options)}):')
    # Display key, values in available options:
    for key, operator in options.items():
        print(f'({key}):{operator.title()}', end=', ')
    # Validate user input:
    while user_input := input('\n>> '):
        # If user_input is not validate then show error-message and continue asking for input
        if not user_input.isdigit() or int(user_input) not in options:
            print(f'Invalid input! Enter a digit between (1-{len(options)})!', file=sys.stderr)
            continue
        else:
            # If user_input is valid, break
            break
    # returns user's option
    return options.get(int(user_input))

# TODO: Make thi smore universal
def get_numeric_input(qty=None, operation=None) -> list:
    """Aks user for two integer inputs, and returns those values"""
    ht = {1: '1st', 2: '2nd'}
    numeric_input = []
    while len(numeric_input) != qty:
        user_input = input(f'Enter {ht.get(len(numeric_input) + 1)} digit:\n>> ')
        if not user_input.isdigit():
            print('Invalid input! Enter a digit (0-9)', file=sys.stderr)
            continue
        else:
            numeric_input.append(int(user_input))
    return numeric_input


print(get_numeric_input(2))
#
#
# def highlight(self):
#     """teal color font"""
#     return f"\033[36m{self}\033[0m"
#
#
# def main():
#     calc = Calculator()
#     while True:
#         mathematical_operation = get_display_options()
#         if mathematical_operation == 'quit':
#             print('Goodbye!')
#             sys.exit()
#         # This is to display the symbol of the mathematical operation the user selects:
#         symbol = {'addition': '+',
#                   'subtraction': '-',
#                   'multiplication': '*',
#                   'division': '÷',
#                   'modulus': '%',
#                   'exponent': '**',
#                   }
#
#        # if mathematical_operation == 'percentage':
#
#
#
#         # Displays what mathematical operation the user choice:
#         print(highlight(f'{symbol.get(mathematical_operation)} {mathematical_operation.title()} Mode'))
#         # Assign self.n1, self.n2 to input values:
#         #TODO make a single varibale
#         calc.n1, calc.n2 = get_numeric_input(mathematical_operation)
#         match mathematical_operation:
#             case 'addition':
#                 print(highlight(f'>> Output: {calc.addition()}'))
#             case 'subtraction':
#                 print(highlight(f'>> Output: {calc.subtraction()}'))
#             case 'multiplication':
#                 print(highlight(f'>> Output: {calc.multiplication()}'))
#             case 'division':
#                 print(highlight(f'>> Output: {calc.division()}'))
#             case 'modulus':
#                 print(highlight(f'>> Output: {calc.modulus()}'))
#             case 'exponent':
#                 print(highlight(f'>> Output: {calc.exponents()}'))
#
#
# if __name__ == '__main__':
#     main()
