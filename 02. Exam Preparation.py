def exam_preparation(bad_grade_count, task_name, task_grade):
    bad_grade_counter = 0
    total_grade = 0
    tasks_counter = 0
    last_problem = ""

    while not task_name == "Enough":

        if bad_grade_counter == bad_grade_count:
            return f"You need a break, {bad_grade_counter} poor grades."

        if task_grade <= 4:
            bad_grade_counter += 1

        total_grade += task_grade
        tasks_counter += 1
        last_problem = task_name
        task_name = input()
        task_grade = float(input())


    average_grade = total_grade / tasks_counter
    return f"Average score: {average_grade:.2f}\nNumber of problems: {tasks_counter}\nLast problem:\n{last_problem}"


bad_grade_count_arg = int(input())
task_name_arg = input()
task_grade_arg = int(input())
print(exam_preparation(bad_grade_count_arg, task_name_arg, task_grade_arg))
