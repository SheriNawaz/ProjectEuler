"""
Task 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""


def main():
    longest_sequence = 0
    start_number = 0
    for i in range(1, 1000000):
        n = i
        length = 1
        while n > 1:  # Generate collatz sequence and calculate length
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            length += 1
        if length > longest_sequence:  # If length is longer than length of longest sequence, use that as current longest
            longest_sequence = length
            start_number = i
    print(start_number)


main()
