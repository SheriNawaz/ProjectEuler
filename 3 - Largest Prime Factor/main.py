import math

def main():
    number = 600851475143
    primes = []
    if number % 2 == 0:
        primes.append(2)
    for i in range(3, math.ceil(number**0.5), 2):
        if is_prime(i) and (number % i) == 0:
            primes.append(i)
    print(primes[len(primes) - 1])


def is_prime(n):
    for i in range(2, math.ceil(n**0.5)):
        if (n % i) == 0:
            return False
    return True


main()
