#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function calculates the factorial of a non-negative integer
    using a recursive approach.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)

