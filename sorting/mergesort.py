"""Merge sort"""

"""Worst-case performance — O(n * log(n))
   Best-case performance  — O(n * log(n))"""

import random
import unittest

# Functions

def merge_sort(array):
    if len(array) < 2:
        return array

    result = []
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)

    result += left
    result += right
    return result


# Tests

random_unsorted_list = [random.randint(0, 1000) for n in range(1000)]

class TestInsertion(unittest.TestCase):
    """Test them all"""

    def test_merge_sort(self):
        """Test for merge sort algorithm"""
        self.assertEqual(merge_sort(random_unsorted_list), 
                         sorted(random_unsorted_list))

if __name__ == '__main__':
    unittest.main()
