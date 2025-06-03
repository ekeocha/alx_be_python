task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

yesno_list =["yes", "no"]

if time_bound not in yesno_list:
	print(f"Incorrect time_bound value -{time_bound}")
	
else:
	match priority:
		case "high":
			if time_bound == "yes":
				print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
			else:
				print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")	
  
		case "medium":
			if time_bound == "yes":
				print(f"Reminder: '{task}' is a {priority} priority task that requires your attention!")
			else:
				print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
            
		case "low":
			if time_bound == "yes":
				print(f"Reminder: '{task}' is a {priority} priority task that requires your attention!")
			else:
				print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
	        	
		case _ :
			print(f"Incorrect priority value -{priority}")
