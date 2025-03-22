def print_until_stop():
    while True:
        # Read input from the user
        user_input = input()

        # Check if the input is "Stop"
        if user_input.lower() == "stop":
            break

        # Print the input
        print(user_input)


# Run the program
print_until_stop()
