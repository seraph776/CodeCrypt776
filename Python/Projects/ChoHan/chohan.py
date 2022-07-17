#!/usr/bin/env python3
"""project:Cho-Han from "Big Book of Small Python Projects" by Al Sweigart, created:1/26/2022, author:seraph★776"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'Go', 6: 'ROKU'}


def main():
    print('''CHo-Han
    
    In this traditional Japanese dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor.
    The player must guess if the dice total tro an even (cho) or odd (han) number.
    ''')

    purse = 5000

    while True:  # Main loop
        # PLace your bet:
        print(f'YOu have {purse}, mon. How much do you want to bet? (or QUIT)')
        while True:
            pot = input('> ')
            if pot.upper() == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            elif not pot.isdecimal():
                print('PLease enter a number')
            elif int(pot) > purse:
                print("You don't have enough to make that bet")
            else:
                # This is a valid bet
                pot = int(pot)  # Convert pot to an integer
                break  # Exit the loop once a valid bet is placed!

        # Roll the dice
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        print('The dealer swirls the cup and you hear the rattle of the dice.')
        print('The dealer slams the cup on the floor, still covering the dice and asks for your bet')
        print()
        print('CHO (even) or HAN (odd)?')

        # Let the player bet cho or han:
        while True:
            bet = input('> ').upper()
            if bet != 'CHO' and bet != 'HAN':
                print('Please enter either "CHO" or "HAN"')
                continue
            else:
                break

        # Reveal the dice results
        print('The dealer lifts the cup to reveal: ')
        print(f'\t{JAPANESE_NUMBERS[d1]} - {JAPANESE_NUMBERS[d2]}')
        print(f'\t{d1} - {d2}')

        # Determine if the player won:
        roll_is_even = (d1 + d2) % 2 == 0
        if roll_is_even:
            correct_bet = 'CHO'
        else:
            correct_bet = 'HAN'

        player_won = bet == correct_bet

        # Display results
        if player_won:
            print(f'You won! You take {pot} mon!')
            purse += pot  # Add the pot from the player's purse
            print(f'The house collects a {pot // 10} mon fee.')
            purse = purse - (pot // 10)  # The house fee is 10%
        else:
            purse -= pot  # Subtract the pot from teh player's purse
            print('You lost!')

        # Check if the player has run out of money
        if purse == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()


if __name__ == '__main__':
    main()
