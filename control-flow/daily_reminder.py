#script that uses conditions and match cases to remind user about priority tasks for the day

task = input('Enter your task: ')
priority = input('Level of priority (high/medium/low): ')
time_bound = input('Is it time-bound? (yes/no): ')

#use match case to check for time-bound tasks

match priority:
    case "high":
        reminder = (f"'{task}', is a high priority task.")
    case "medium":
        reminder = (f"'{task}' is a medium priority task.")
    case "low":
        reminder = (f"'{task}' is a low priority task.") 
    case _:
        reminder = print('Priority is invalid.')

# use if statements to set more conditions:

if priority == 'high' and time_bound == 'yes':
    print(f'{reminder} It requires immediate attention today!')
elif priority == 'high' and time_bound != 'yes':
    print(f"{reminder} You should do as soon as possible!")
elif priority == 'medium' and time_bound == 'yes':
    print(f'{reminder} Do it before the day is done.')
elif priority == 'medium' and time_bound != 'yes':
    print(f"{reminder} Remember to finish it before it's too late")
elif priority == 'low' and time_bound == 'yes':
    print(f'{reminder} Allocate time to finish it when you can.')
else:
    print(reminder)
