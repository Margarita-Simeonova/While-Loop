import sys


def max_number(data):
    biggest_number = -sys.maxsize

    while not data == "Stop":
        number = int(data)
        if number > biggest_number:
            biggest_number = number

        data = input()

    return biggest_number


data_arg = int(input())
result = max_number(data_arg)
print(result)
