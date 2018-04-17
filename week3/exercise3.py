"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


<<<<<<< HEAD
=======
from exercise1 import not_number_rejector
from exercise1 import super_asker
>>>>>>> a0fec480311b6bb045bdb79ae1c35177118a8ce3
import random

import os
import sys
print(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from week3.exercise1 import not_number_rejector

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nwelcome to the guessing game!")
    print("A number between _? and _ ?")
    lowerBound = not_number_rejector("Enter an lower bound: ")

    flag = False
    while not flag:
        upperBound = not_number_rejector("Enter an upper bound: ")
        if (upperBound>=lowerBound):
          flag = True
        else:
          print("the upperBound is less than lowerBound")

    print("OK then, a number between {} and {} ?".format(lowerBound,upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    xstr = ""
    while not guessed:
      try:
        xstr = input("guess a number: ")
        guessedNumber = int(xstr)
        print("you guessed {},".format(guessedNumber),)
        if (guessedNumber == actualNumber):
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("too small, try again ")
        else:
            print("too big, try again   ")
      except Exception:
        print("you entered {} is not a number".format(xstr))

    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
