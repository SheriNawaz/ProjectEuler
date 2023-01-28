"""
Task 9
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def main():
    # m and n are used to generate Pythagorean triples using Euclid's formula
    for m in range(1, 32):
        for n in range(1, m):
            # Euclid's formula for generating a Pythagorean triple: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n^2
            # check if the sum of a, b, and c equals 1000
            if a+b+c == 1000:
                print("FOUND")
                print(a*b*c)
                return

main()
