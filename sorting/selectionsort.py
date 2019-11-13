"""Selection sort"""

"""Worst-case performance — O(n**2) comparisons or 0(n) swaps
   Best-case performance  — O(n**2) comparisons or 0(n) swaps"""

import random
import unittest

# Functions

def selection_sort(sequence):
    """Simple selection sorting"""
    for i in range(0, len(sequence)):
        minimum = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[minimum]:
                minimum = j
        if minimum != i:
            sequence[minimum], sequence[i] = (sequence[i], 
            sequence[minimum])
    return sequence
    
# Tests

random_unsorted_list = [random.randint(0, 1000) for n in range(1000)]

class TestSelection(unittest.TestCase):
    """Test them all"""

    def test_selection_sort(self):
        """Test for insertion sort algorithm"""
        self.assertEqual(selection_sort(random_unsorted_list), 
                         sorted(random_unsorted_list))

if __name__ == '__main__':
    unittest.main()
