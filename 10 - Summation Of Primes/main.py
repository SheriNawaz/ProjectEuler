"""
Task 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def main():
    sum = 2
    for i in range(3, 2000000, 2):
        if is_prime(i):
            print(i)
            sum += i
    print(sum)


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i then n isn't a prime number
        if (n % i) == 0:
            return False
    return True


main()
