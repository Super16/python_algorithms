"""Closest pair of points problem"""

"""Average performance — O(n**2)"""

import math

def closest_pair(array_of_points):
    """Brute-force finding closest pair of points and distance inbetween  
       in two dimensions"""
    minimal_distance = float("inf")
    first_point = None
    second_point = None
    length = len(array_of_points)
    for i in range(length - 1):
        for j in range(i + 1, length):
            pair = distance(array_of_points[i], array_of_points[j])
            if pair < minimal_distance:
                first_point = array_of_points[i]
                second_point = array_of_points[j]
                minimal_distance = pair
    return first_point, second_point, minimal_distance

def distance(first_point, second_point):
    """Euclidean distance between two points"""
    return math.sqrt((second_point[0] - first_point[0]) ** 2 + 
    (second_point[1] - first_point[1]) ** 2)
