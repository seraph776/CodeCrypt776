#!/usr/bin/env python3
"""
project: Hangman
created:2022-1-1
@author:seraph1001100
email:seraph1001100@gmail.com
"""

from random import choice
from hangman import hangmanIMAGE

animals = ['tiger', 'lion', 'giraffe', 'zebra', 'dolphin', 'shark', 'elephant', 'rhino']

word = choice(animals).lower()

guessed_correctly = []
guessed_incorrectly = []
tries = 6
hangman_count = -1

while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ '

    if output == word:
        break

    print(f"Guess the word: {output}")
    print(f"{tries} chances left")

    guess = input().lower()

    if guess in guessed_correctly or guess in guessed_incorrectly:
        print(f"Already guessed {guess}")
    elif guess in word:
        print("Awesome job! You guessed a correct letter")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You guessed a wrong letter!")
        hangman_count += 1
        tries -= 1
        guessed_incorrectly.append(guess)
        print(hangmanIMAGE[hangman_count])

if tries > 0:
    print("You guessed the word correctly! You win!")
else:
    print("Sorry you guessed the wrong letter. Try again.")
