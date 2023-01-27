"""
Task 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import math


def main():
    primes = [1, 2]
    i = 3
    while len(primes) <= 10001:
        if is_prime(i):
            print(i)
            primes.append(i)
        i += 2
    print(primes[len(primes) - 1])


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i then n isn't a prime number
        if (n % i) == 0:
            return False
    return True


main()
