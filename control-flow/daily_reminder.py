# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("What is the task's priority? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Begin response based on priority using match-case
match priority:
    case "high":
        reminder = f"⚠️ High priority task: {task}."
    case "medium":
        reminder = f"📝 Medium priority task: {task}."
    case "low":
        reminder = f"📌 Low priority task: {task}."
    case _:
        reminder = f"❓ Task: {task} has an unknown priority level."

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Display the customized reminder
print("\nDaily Reminder:")
print(reminder)
