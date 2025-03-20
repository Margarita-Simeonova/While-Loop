# Read the initial inputs
money_needed = float(input())
money_available = float(input())

# Initialize counters
days_elapsed = 0
consecutive_spend_days = 0

# Loop until Jessie saves enough money or spends for 5 consecutive days
while money_available < money_needed and consecutive_spend_days < 5:
    days_elapsed += 1
    action = input()
    amount = float(input())

    if action == "save":
        money_available += amount
        consecutive_spend_days = 0  # Reset consecutive spend days
    elif action == "spend":
        money_available -= amount
        if money_available < 0:
            money_available = 0  # Jessie cannot have negative money
        consecutive_spend_days += 1
    else:
        print("Invalid action. Please enter 'spend' or 'save'.")
        continue


# Check the exit conditions
if consecutive_spend_days >= 5:
    print("You can't save the money.")
    print(f"{days_elapsed}")
elif money_available >= money_needed:
    print(f"You saved the money for {days_elapsed} days.")
