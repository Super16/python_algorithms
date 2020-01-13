"""Quick sort"""

"""Worst-case performance — O(n ** 2)
   Best-case performance  — O(n * log(n))"""

import random
import unittest

# Functions

def quicksort(array):
    _quicksort(array, 0, len(array) - 1)
    return array

def _quicksort(array, low, high):
    if low < high:    
        pivot = partition(array, low, high)
        _quicksort(array, low, pivot - 1)
        _quicksort(array, pivot + 1, high)

def partition(array, low, high):
    pivot = array[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i - 1], array[low] = array[low], array[i - 1]
    return i - 1

# Tests

random_unsorted_list = [random.randint(0, 1000) for n in range(1000)]

class TestInsertion(unittest.TestCase):
    """Test them all"""

    def test_quicksort(self):
        """Test for quicksort algorithm"""
        self.assertEqual(quicksort(random_unsorted_list), 
                         sorted(random_unsorted_list))

if __name__ == '__main__':
    unittest.main()
