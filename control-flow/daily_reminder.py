#script that uses conditions and match cases to remind user about priority tasks for the day

task = input('Enter your task: ')
priority = input("Priority (high/medium/low): ")
time_bound = input('Is it time-bound? (yes/no): ')

task = task
priority = priority
time_bound = time_bound

#use match case to check for time-bound tasks
# use if statements to set more conditions:

match priority:
    case "high":
        reminder = (f"'{task}', is a high priority task.")
        if time_bound == 'yes':
            customized = 'It requires immediate attention today!'
            print(f" Reminder: {reminder} {customized}")
        elif time_bound != 'yes':
            
            print(f"{reminder} You should do it as soon as possible!")
        else:
            print(reminder)

    case "medium":
        reminder = (f"'{task}' is a medium priority task.")
        if priority == 'medium' and time_bound == 'yes':
            print(f'{reminder} Do it before the day is done.')
        elif priority == 'medium' and time_bound != 'yes':
            print(f"{reminder} Remember to finish it before it's too late")
        else:
            print(reminder)

    case "low":
        reminder = (f"'{task}' is a low priority task.") 
        if priority == 'low' and time_bound == 'yes':
            print(f'{reminder} Allocate time to finish it when you can.')
        else:
            print(reminder)

    case _:
        reminder = print('Priority is invalid.')






