# daily_reminder.py with nested loops

while True:
    print("\nLet's add a new task:")

    # Inner loop: handles one task at a time
    while True:
        task = input("Enter your task: ")
        priority = input("What is the task's priority? (high/medium/low): ").lower()
        time_bound = input("Is this task time-bound? (yes/no): ").lower()

        # Match case to handle priority levels
        match priority:
            case "high":
                reminder = f"⚠️ High priority task: {task}."
            case "medium":
                reminder = f"📝 Medium priority task: {task}."
            case "low":
                reminder = f"📌 Low priority task: {task}."
            case _:
                reminder = f"❓ Task: {task} has an unknown priority level."

        # Time-bound check
        if time_bound == "yes":
            reminder += " This task requires immediate attention today!"

        # Print the reminder
        print("\nDaily Reminder:")
        print(reminder)

        break  # Breaks the inner loop after one task is processed

    # Ask if user wants to add another task
    add_another = input("\nWould you like to add another task? (yes/no): ").lower()
    if add_another != "yes":
        print("✅ Task reminder setup complete. Have a productive day!")
        break  # Breaks the outer loop and ends the program
