# Gabby's daily step goal
step_goal = 10000
total_steps = 0

while True:
    # Read steps or the "Going home" command
    steps_input = input()

    if steps_input.lower() == "going home":
        # Read steps walked on the way home
        steps_home = int(input())
        total_steps += steps_home # Gabby is going home, so exit the loop
        if total_steps < step_goal:
            break
    else:
        # Add steps walked
        steps = int(steps_input)
        total_steps += steps

    # Check if the goal is reached
    if total_steps >= step_goal:
        print("Goal reached! Good job!")
        print(f"{total_steps - step_goal} steps over the goal!")
        break  # Exit the program

# If Gabby goes home before reaching the goal
if total_steps < step_goal:
    print(f"{step_goal - total_steps} more steps to reach goal.")
    