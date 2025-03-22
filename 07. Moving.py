def calculate_free_volume():
    # Input: Dimensions of the free space
    width = int(input())
    length = int(input())
    height = int(input())

    # Calculate total free volume in cubic meters
    total_volume = width * length * height

    # Initialize variables
    used_volume = 0

    # Loop to move boxes until free space runs out or "Done" is entered
    while True:
        command = input()

        if command.lower() == "done":
            if used_volume < total_volume:
                free_volume = total_volume - used_volume
                print(f"{free_volume} Cubic meters left.")
            break

        boxes = int(command)
        used_volume += boxes  # Each box occupies 1 cubic meter

        if used_volume >= total_volume:
            missing_volume = used_volume - total_volume
            print(f"No more free space! You need {missing_volume} Cubic meters more.")
            break


# Run the program
calculate_free_volume()
