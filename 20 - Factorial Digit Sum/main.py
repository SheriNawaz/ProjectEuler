"""
Task 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def main():
    # Get 100!
    factorial = 1
    for i in range(1, 101):
        factorial *= i
    digits = [int(i) for i in str(factorial)]  # Split number into digits
    sum = 0
    for i in digits:
        sum += i  # Add digits
    print(sum)


main()
