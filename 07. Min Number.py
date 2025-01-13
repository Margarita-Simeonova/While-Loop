import sys


def min_number(data):
    smallest_number = sys.maxsize

    while not data == "Stop":
        number = int(data)
        if number < smallest_number:
            smallest_number = number

        data = input()

    return smallest_number


data_arg = int(input())
result = min_number(data_arg)
print(result)
