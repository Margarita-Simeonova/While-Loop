def cake_party():
    # Input: Cake dimensions (width and length)
    width = int(input())
    length = int(input())

    # Calculate total cake pieces
    total_pieces = width * length

    # Initialize variables
    pieces_taken = 0

    # Loop to take pieces until cake runs out or "STOP" is entered
    while True:
        command = input()

        if command == "STOP":
            if pieces_taken < total_pieces:
                print(f"{total_pieces - pieces_taken} pieces are left.")
            break

        try:
            pieces = int(command)
            pieces_taken += pieces

            if pieces_taken >= total_pieces:
                missing_pieces = pieces_taken - total_pieces
                print(f"No more cake left! You need {missing_pieces} pieces more.")
                break
        except ValueError:
            print("Invalid input. Please enter a number or 'STOP'.")


# Run the program
cake_party()
