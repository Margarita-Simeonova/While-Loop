def sequence_2k_plus_1(number):
    counter = 1
    while counter <= number:
        print(counter)
        result = counter * 2 + 1
        counter = result


number_arg = int(input())
sequence_2k_plus_1(number_arg)
