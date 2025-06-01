# daily_reminder.py

task = input("Enter your task for today: ")
priority = input("What is the task’s priority? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print(f"🔴 High Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "medium":
        print(f"🟡 Medium Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case "low":
        print(f"🟢 Low Priority Task: {task}")
        if time_bound == "yes":
            print("This task requires immediate attention today!")
    case _:
        print(f"⚪ Task: {task} (Priority not recognized)")
        if time_bound == "yes":
            print("This task requires immediate attention today!")

