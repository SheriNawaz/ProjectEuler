"""
Task 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

import math


def main():
    grid_size = 20
    # Working out the combination of a set of directions
    n = grid_size * 2 # Directions per set
    r = grid_size # Amount in each sub-set (the number of times you move right is equal to times you move down)
    # Use nCr formula to work out number of routs
    num_routes = (math.factorial(n))/(math.factorial(r) * math.factorial(n-r))
    print(num_routes)


main()
