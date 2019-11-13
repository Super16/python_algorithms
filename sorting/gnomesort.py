"""Gnome sort"""

"""Worst-case performance — O(n**2)
   Best-case performance  — O(n)"""

import random
import unittest

# Functions

def gnome_sort(sequence):
    """Simple gnome sorting"""
    i = 0
    while i < len(sequence):
        if i == 0 or sequence[i - 1] <= sequence[i]:
            i += 1
        else:
            sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
            i -= 1
    return sequence


# Tests

random_unsorted_list = [random.randint(0, 1000) for n in range(1000)]


class TestGnome(unittest.TestCase):
    """Test them all"""

    def test_gnome_sort(self):
        """Test for gnome sort algorithm"""
        self.assertEqual(gnome_sort(random_unsorted_list), 
                         sorted(random_unsorted_list))

if __name__ == '__main__':
    unittest.main()
