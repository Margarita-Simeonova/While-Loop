def vacation(vacation_money: float):
    money_have = float(input())
    days_counter = 0
    is_money_spend = True
    spend_counter = 0

    while True:

        command = input()
        money = float(input())
        days_counter += 1

        if command == "spend":
            money_have -= money
            spend_counter += 1
            if money_have < 0:
                money_have = 0

            if spend_counter == 5:
                is_money_spend = False
                break

        else:
            money_have += money

        if money_have >= vacation_money:
            break

    if is_money_spend:
        return f"You saved the money for {days_counter} days."
    return f"You can't save the money.\n{days_counter}"


vacation_money_arg = float(input())

result = vacation(vacation_money_arg)
print(result)
