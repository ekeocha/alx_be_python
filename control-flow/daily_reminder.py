# daily reminder

task = input("Enter task for today: ")
priority = input("whats the priority level (high, medium, low) ") 
time_bound = input("is this task time bound (Yes/No)")


match priority:
    case "high":
        print(f" High Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "medium":
        print(f" Medium Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "low":
        print(f"Low Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")