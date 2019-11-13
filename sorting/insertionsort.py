"""Insertion sort"""

"""Worst-case performance — O(n**2)
   Best-case performance  — O(n) comparisons or 0(1) swaps"""

import random
import unittest

# Functions

def insertion_sort(sequence):
    """Simple insertion sorting"""
    for i in range(1, len(sequence)):
        j = i
        while j > 0 and sequence[j - 1] > sequence[j]:
            sequence[j - 1], sequence[j] = sequence[j], sequence[j - 1]
            j -= 1
    return sequence


# Tests

random_unsorted_list = [random.randint(0, 1000) for n in range(1000)]

class TestInsertion(unittest.TestCase):
    """Test them all"""

    def test_insertion_sort(self):
        """Test for insertion sort algorithm"""
        self.assertEqual(insertion_sort(random_unsorted_list), 
                         sorted(random_unsorted_list))

if __name__ == '__main__':
    unittest.main()
