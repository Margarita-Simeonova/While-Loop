def sum_numbers(control_number):
    global sum_numbs
    try:
        number = int(input())
        sum_numbs = number

        while sum_numbs < control_number:
            number = int(input())
            sum_numbs += number

        return sum_numbs
    except KeyboardInterrupt:

        return sum_numbs


number = int(input())
print(sum_numbers(number))
