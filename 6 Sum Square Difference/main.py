"""
Task 6
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():
    #Get sum of squares of all numbers between 1 and 100

    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i ** 2

    #Get square of sum of all numbers between 1 and 100
    sum = 0
    for i in range(1, 101):
        sum += i
    square_of_sum = sum ** 2

    #Print out difference
    print(square_of_sum - sum_of_squares)


main()
