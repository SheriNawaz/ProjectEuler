"""
Task 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""


def main():
    num = 2 ** 1000
    digits = [int(i) for i in str(num)]
    sum = 0
    for i in digits:
        sum += i
    print(sum)


main()
