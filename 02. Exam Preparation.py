def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0  # Prevent division by zero

def process_exam(max_poor_grades):
    poor_grades = 0
    total_problems = 0
    grades = []
    last_problem = ""

    problem_name = input()  # Read the first problem
    while problem_name != "Enough" and poor_grades < max_poor_grades:
        grade = int(input())
        grades.append(grade)
        total_problems += 1
        last_problem = problem_name

        if grade <= 4:
            poor_grades += 1

        if poor_grades < max_poor_grades:  # Only read the next problem if still allowed
            problem_name = input()

    if problem_name == "Enough":  # If stopped by "Enough"
        average_score = calculate_average(grades)
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {total_problems}")
        print(f"Last problem: {last_problem}")
    else:  # If stopped by exceeding poor grades
        print(f"You need a break, {poor_grades} poor grades.")


# Read the maximum number of poor grades allowed
max_poor_grades_arg = int(input())
process_exam(max_poor_grades_arg)
