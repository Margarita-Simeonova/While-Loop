def account_balance(installment):
    balance = 0
    while not installment == "NoMoreMoney":
        installment = float(installment)

        if installment < 0:
            return f"Invalid operation!\nTotal: {balance:.2f}"

        print(f"Increase: {installment:.2f}")
        balance += installment

        installment = input()

    return f"Total: {balance:.2f}"


installment_arg = float(input())
print(account_balance(installment_arg))
