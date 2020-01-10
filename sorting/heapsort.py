"""Heapsort sort"""

"""Worst-case performance — O(n * log(n))
   Best-case performance  — O(n * log(n))"""

from heapq import heappush, heappop
import random
import unittest

# Functions

def heapify(array, lenght, i):
    """Heapify the subtree at index i"""
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2 
  
    if left < lenght and array[largest] < array[left]: 
        largest = left
  
    if right < lenght and array[largest] < array[right]: 
        largest = right
  
    if largest != i: 
        array[i], array[largest] = array[largest], array[i] 
        heapify(array, lenght, largest)

def heapsort(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
    return array

# Tests

random_unsorted_list = [random.randint(0, 1000) for n in range(1000)]

def embedded_heapsort(array):
    """Basic example of heapsort from python docs"""
    heap = []
    for value in array:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]

class TestHeapsort(unittest.TestCase):
    """Test them all"""

    def test_heapsort(self):
        """Test for heapsort algorithm with sorting function and 
           standard heapq implementation"""
        self.assertEqual(heapsort(random_unsorted_list), 
                         sorted(random_unsorted_list))
        self.assertEqual(heapsort(random_unsorted_list), 
                         embedded_heapsort(random_unsorted_list))

if __name__ == '__main__':
    unittest.main()
