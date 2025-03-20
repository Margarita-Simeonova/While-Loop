# def coins(change):
#     change *= 100
#
#     number_of_coins = 0
#
#     number_of_coins += change // 200
#     change %= 200
#     number_of_coins += change // 100
#     change %= 100
#     number_of_coins += change // 50
#     change %= 50
#     number_of_coins += change // 20
#     change %= 20
#     number_of_coins += change // 10
#     change %= 10
#     number_of_coins += change // 5
#     change %= 5
#     number_of_coins += change // 2
#     change %= 2
#     number_of_coins += change
#
#     return round(number_of_coins)
#
#
# change_arg = float(input())
# result = coins(change_arg)
# print(result)


def coins(change):
    # Convert euros to cents and handle floating-point precision
    change = int(round(change * 100))

    # Euro coin denominations in cents
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    number_of_coins = 0

    # Calculate the minimum number of coins
    for coin in denominations:
        number_of_coins += change // coin
        change %= coin

    return number_of_coins

# Example usage
change_arg = float(input())
result = coins(change_arg)
print(result)