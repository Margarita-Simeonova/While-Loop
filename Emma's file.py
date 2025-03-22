# Step 1: Ask for two numbers
print("Let's add two two-digit numbers!")
num1 = int(input("Enter the first: "))
num2 = int(input("Enter the second number: "))

# Step 2: Break the numbers into tens and ones
tens1 = num1 // 10
ones1 = num1 % 10
tens2 = num2 // 10
ones2 = num2 % 10

# Step 3: Add the ones place
ones_sum = ones1 + ones2
carry_over = ones_sum // 10
ones_result = ones_sum % 10

# Step 4: Add the tens place
tens_sum = tens1 + tens2 + carry_over
tens_result = tens_sum % 10
final_carry = tens_sum // 10

# Step 5: Combine the results
final_result = final_carry * 100 + tens_result * 10 + ones_result

# Step 6: Show the steps and result
print("\nLet's see how we add them:")
print(f"  First, add the ones place: {ones1} + {ones2} = {ones_sum}")
if carry_over:
    print(f"    Since {ones_sum} is 10 or more, we write down {ones_result} and carry over {carry_over}.")
else:
    print(f"    We write down {ones_result}.")

print(f"  Next, add the tens place: {tens1} + {tens2} + {carry_over} = {tens_sum}")
if final_carry:
    print(f"    Since {tens_sum} is 10 or more, we write down {tens_result} and carry over {final_carry}.")
else:
    print(f"    We write down {tens_result}.")

print(f"\nThe final answer is: {final_result}")