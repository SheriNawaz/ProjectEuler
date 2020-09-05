"""

    Title: Even Fibonacci
    Author: Sheriyar Nawaz
    Date: August 2020
    Description: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the
    sum of the even-valued terms.

"""


def main():
    prev_term = 1
    term = 1
    sum = 0
    while term < 4000000:
        temp = term
        term = term + prev_term
        prev_term = temp
        if term % 2 == 0:
            sum += term
    print(sum)


if __name__ == '__main__':
    main()