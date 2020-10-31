'''

  Name: Largest Prime Factor
  Author: Sheri Nawaz
  Description: The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143 ?
  Date: October 2020

'''


def is_prime(num):
  for i in range(1, num - 1, 2):
    if i != 1 and num % i == 0:
      return False
  return True


def largest_prime_factor(num):
  prime_factors = []

  for i in range(1, num):
    if num % i == 0:
      if is_prime(i):
        print(i)
        prime_factors.append(i)

largest_prime_factor(600851475143)
