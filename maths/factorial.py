"""Factorial"""

"""Factorial of a positive integer n, denoted by n!, is the product 
   of all positive integers less than or equal to n"""

import math
import random
import unittest

# Functions

def factorial(input_number, f = 1):
    """Iterative factorial function"""
    for i in range(1, input_number + 1): 
        f = f * i
    return f

def recursive_factorial(input_number):
    """Recursive factorial function, doesn't work with input
    number > 998 by default, because of default CPython recursion limit
    """
    if input_number == 1:
        return input_number
    else:
        return input_number * recursive_factorial(input_number - 1)
        
# Tests

random_input = random.randint(0, 998)

class TestFactorial(unittest.TestCase):
    """Test them all"""

    def test_factorial(self):
        """Test with math module factorial method"""
        self.assertEqual(factorial(random_input), 
        math.factorial(random_input))
        self.assertEqual(recursive_factorial(random_input), 
        math.factorial(random_input))

if __name__ == '__main__':
    unittest.main()
