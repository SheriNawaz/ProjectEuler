"""
Task 6
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i ** 2
    sum = 0
    for i in range(1, 101):
        sum += i
    square_of_sum = sum ** 2

    print(square_of_sum - sum_of_squares)


main()
