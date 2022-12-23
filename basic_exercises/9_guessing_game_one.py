"""

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random
import sys


def guess_number(user_guess, rand_number, tries):
    """
    Method determines if the user_guess matches the rand_number
    :param user_guess:
    :param rand_number:
    :param tries
    :return: basestring
    """

    if user_guess < rand_number:
        return "Too low!"
    if user_guess > rand_number:
        return "Too high!"
    if user_guess == rand_number:
        return "You guessed correctly and it took you " + str(tries) + " tries"
    else:
        sys.exit()


def get_random_number(start, end):
    """
    Gets a random number between a range of numbers
    :rtype: int
    """
    return random.randint(start, end)


random_number = get_random_number(1, 9)
count = 0
guess = 0

while guess != random_number and guess != 'q':
    guess = int(input('Guess a number between 1 and 9 '))

    if guess == 'q':
        break

    count += 1
    print(guess_number(guess, random_number, count))
    print()
