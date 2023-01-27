"""
Task 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


import math


def main():
    number = 600851475143
    primes = []
    if number % 2 == 0:
        primes.append(2)
    """ Loop through every odd number from 3 to the square root of number (as these are all of the possible numbers
    that number can be divisible by) """
    for i in range(3, math.ceil(number ** 0.5), 2):
        if is_prime(i) and (number % i) == 0:
            primes.append(i)
    print(primes[len(primes) - 1])  # Print last number of primes list


def is_prime(n):
    for i in range(2, math.ceil(n ** 0.5)):
        # If n is divisible by i then n isn't a prime number
        if (n % i) == 0:
            return False
    return True


main()
