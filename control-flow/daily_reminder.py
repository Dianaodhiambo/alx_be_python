# daily_reminder.py

# Prompt the user to enter a task description
task = input("Enter your task: ")

# Prompt the user to enter the task's priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to react based on the task's priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Check if the task is time-bound and modify the reminder accordingly
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder with the required phrase
print(f"Reminder: {reminder}")

