# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    Each guess, print what the guess is Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    This will be quite hard, especially hard if you don't have a good diagram!

    Debugging helpers:
      * GUARD is there to make it only run a few times so that you can see
        what's happening.
      * time.sleep(0.5) makes it pause for half a second.
      You don't need to use both together, and should remove them both before
      you submit. The tests will be checking that they aren't in there.
      (You should remove them from the file, not comment them out, the
      tests aren't that smart yet.)
    """
<<<<<<< HEAD
    tries = 1
    guess = actual_number

=======

    return {"guess": guess, "tries": tries}
>>>>>>> a0fec480311b6bb045bdb79ae1c35177118a8ce3

    if ((guess<low) or (guess>high)):
      return { }
    start = low
    end = high
    while(start<=end):
      mid = int( (start+end)/2 )
      if ((guess==mid) or (guess==start) or (guess==end)):
        print("got it[{}] by [{}] times".format(guess,tries))
        return {"guess": guess, "tries": tries}
      elif ( guess < mid ):
        end   = mid-1
        start =start+1
      else:
        start = mid+1
        end = end-1
      tries = tries+1
    return { }

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
