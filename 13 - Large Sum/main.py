"""
Task 13
Work out the first ten digits of the sum of the 100 50-digits numbers
"""


def main():
    # Convert file into array of numbers
    with open('numbers.txt', 'r') as f:
        data = f.read()
    numbers = data.split()

    # Add together all numbers
    sum_of_nums = 0
    for i in range(0, len(numbers)):
        sum_of_nums += int(numbers[i])

    # Print out first 10 digits of sum
    print(int(str(sum_of_nums)[:10]))


main()
