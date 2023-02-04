"""
Task 18
Find the maximum total from top to bottom of the triangle
"""


def main():
    with open('triangle.txt', 'r') as f:
        data = [list(map(int, line.strip().split())) for line in f]

    for i in range(len(data) - 2, -1, -1):
        for j in range(len(data[i])):
            data[i][j] = max(data[i][j] + data[i + 1][j], data[i][j] + data[i + 1][j + 1])

    print("Maximum total:", data[0][0])


main()
