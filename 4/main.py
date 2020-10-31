'''

  Name: Largest Palindrome Product
  Author: Sheri Nawaz
  Description: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
  Find the largest palindrome made from the product of two 3-digit numbers.
  Date: October 2020

'''


def is_palindrome(num):
    forward_nums = []
    for i in range(num):
        forward_nums.append(i)
    # 123456
    backwards_nums = []
    for i in reversed(range(num)):
        backwards_nums.append(i)

    if forward_nums == backwards_nums:
        return True
    else:
        return False


def main():
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if is_palindrome(product):
                print(i + " * " + j + " = " + product)


main()
