"""
Task 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""


def main():
    numbers_to_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    numbers_to_words_2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    sum = 0
    for i in range(1, 1001):
        digits = [int(j) for j in str(i)]  # Split number into digits
        for j in range(0, len(digits)):
            digits[j] = int(digits[j])
        if (len(digits) == 1) or (len(digits) == 2 and digits[0] == 1):  # If number is 1-19
            word = numbers_to_words[i]
            sum += len(word)
            print(i, len(word))
        elif len(digits) == 2 and digits[0] > 1:  # If number is 20-99
            word = numbers_to_words_2[digits[0] - 2]
            word_2 = ""
            if not digits[1] == 0:  # If number ends in 0
                word_2 = numbers_to_words[digits[1]]
            sum += (len(word) + len(word_2))
            print(i, len(word) + len(word_2))
        elif len(digits) == 3:  # If number is between 100-999
            word = ""
            word_2 = ""
            word_3 = ""
            if not digits[1] == 0 or not digits[2] == 0:  # Makes number hundred and
                word_3 = "and"
            if digits[1] == 1:  # For teen numbers
                word = numbers_to_words[int(str(digits[1]) + str(digits[2]))]
            else:
                if not digits[1] == 0:
                    word = numbers_to_words_2[digits[1] - 2]
                if not digits[2] == 0:
                    word_2 = numbers_to_words[digits[2]]
            sum += (len(word) + len(word_2) + len("hundred") + len(word_3) + len(numbers_to_words[digits[0]]))
            print(i, len(word) + len(word_2) + len("hundred") + len(word_3) + len(numbers_to_words[digits[0]]))
        elif i == 1000:
            print(i, len("onethousand"))
            sum += len("onethousand")
        if i == 100:
            print(sum)
    print(len("onehundredandtwelve"))
    print(sum)


main()
