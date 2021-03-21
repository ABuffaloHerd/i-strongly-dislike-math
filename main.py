import math
from commonlib import *

def multiples_in_range():
    """
    How many multiples of x in y? I don't fucking know and i don't fucking care enough to do it myself.
    """
    x = validate_int_v2("Input range to work with: ", None, 1)
    y = validate_int_v2("Multiple of:  ", None, 1)

    range_list = []

    #Generate list from range
    for i in range(1, x):
        if i % y == 0:
            range_list.append(i)
        
    #print
    print(range_list)
    print("Number of multiples is {}" .format(len(range_list)))

def is_square_in_range():
    """
    Regurgitates squares within a set range
    """
    squares = []
    x = validate_int_v2("Input range to work with: ", None, 1)

    for i in range(1, x):
        root = round(math.sqrt(i))

        if root * root == i:
            squares.append(i)

    print(squares)
    print("Number of squares: {}".format(len(squares)))

def is_odd():
    """
    Spits out a list of odd numbers
    """
    odds = []
    x = validate_int_v2("Input range to work with: ", None, 1)

    #Generate list from range
    for i in range(1, x):
        if i % 2 == 1:
            odds.append(i)

    print(odds)
    print("Number of odds: {}".format(len(odds)))

def factor_lookup():
    """
    Finds all the factors of a number
    """
    factor = validate_int_v2("Input factor to work with: ", None, 1)

    factors = []
    for i in range(1, factor + 1):
        if factor % i == 0:
            factors.append(i)

    print(factors)
    print("Number of factors: {}" .format(len(factors)))