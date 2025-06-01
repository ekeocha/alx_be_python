task = input("What's the task for today: ")
priority = input("What's the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time bound (Yes/No): ").lower()

match priority:
    case "high":
        print(f"High Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "medium":
        print(f"Medium Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "low":
        print(f"Low Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case _:
        print("Invalid priority level.")
