"""
Task 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#EXTREMELY INEFFICIENT BUT WORKS

def main():
    num_found = False
    i = 20
    while not num_found:
        for j in range(1, 21):
            if i % j != 0:
                print(i)
                break
            if j == 20 and i % j == 0:
                print(i)
                num_found = True
        i += 20



main()
