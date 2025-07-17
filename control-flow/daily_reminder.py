# daily_reminder.py

# Prompt the user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Display custom reminder based on priority and time-sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to work on it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but time-sensitive. Try to fit it in today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please use 'high', 'medium', or 'low'.")
alx_be_python/
└── control-flow/
    ├── pattern_drawing.py
    └── daily_reminder.py
