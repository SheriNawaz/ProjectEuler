"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def main():
    palindromes = []
    #Multiply every combination of 2 3-digit numbers
    for i in range(100, 1000):
        for j in range(100, 1000):
            result = i * j
            digits = [int(k) for k in str(result)] #Split result into list of digits
            if is_palindrome(digits):
                palindromes.append(result)
    palindromes.sort()
    print(palindromes[len(palindromes) - 1])


def is_palindrome(digits):
    for k in range(0, len(digits)):
        if digits[k] != digits[len(digits) - k - 1]: #If the digit is not equal to the digit on the opposite side, return false
            return False
    return True


main()
