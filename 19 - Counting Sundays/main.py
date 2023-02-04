"""
Task 19
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def main():
    day_counter = 2  # 1st January 1901 was Tuesday
    sundays = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            if month == 4 or month == 6 or month == 9 or month == 11:  # If month is April, June, September, November
                month_length = 30
            elif month == 2:  # If month is February
                if year % 4 == 0:  # If leap year
                    month_length = 29
                else:
                    month_length = 28
            else:
                month_length = 31
            for day in range(1, month_length + 1):
                if day_counter == 7 and day == 1:
                    sundays += 1
                if day_counter < 7:
                    day_counter += 1
                else:
                    day_counter = 1

    print(sundays)


main()
