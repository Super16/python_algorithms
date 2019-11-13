"""Fibonacci numbers"""

"""In Fibonacci sequence each number is the sum of the two 
   preceding ones"""

from functools import lru_cache
import unittest

# Functions

def fibonacci(input_number):
    """Straight-line design, but slowing down with big input_numbers"""
    if input_number < 2:
        return input_number
    return fibonacci(input_number - 2) + fibonacci(input_number - 1) 

@lru_cache(maxsize=None)
def memo_fibonacci(input_number):
    """Same implementation with memoziation, much faster"""
    if input_number < 2:
        return input_number
    return (memo_fibonacci(input_number - 2) + 
            memo_fibonacci(input_number - 1))

def iterative_fibonacci(input_number):
    """Fibonacci numbers iterator"""
    if input_number == 0:
        return input_number
    a, b = 0, 1
    for _ in range(1, input_number):
        a, b = b, a + b
    return b

# Tests


class TestFibonacci(unittest.TestCase):
    """Test them all"""

    def test_fibonacci(self):
        """Slow implementations with small numbers, faster functions 
        with bigger ones"""
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(memo_fibonacci(100), 354224848179261915075)
        self.assertEqual(iterative_fibonacci(100), 
                         354224848179261915075)

if __name__ == '__main__':
    unittest.main()
