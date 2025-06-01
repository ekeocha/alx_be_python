# daily_reminder.py

# This loop ensures the user provides valid input (optional but makes it cleaner)
while True:
    task = input("Enter your task for today: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

priority = input("What is the task’s priority? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Match Case to determine reminder based on priority
match priority:
    case "high":
        reminder = f"🔴 High Priority Task: {task}."
    case "medium":
        reminder = f"🟡 Medium Priority Task: {task}."
    case "low":
        reminder = f"🟢 Low Priority Task: {task}."
    case _:
        reminder = f"⚪ Task: {task} (Priority not recognized)."

# Check if time-bound and update reminder
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Print the final reminder
print("\n🗓️ Daily Reminder:")
print(reminder)

