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
            print(f"Reminder: {reminder} {customized}")
        elif time_bound != 'yes':
            customized = 'You should do it as soon as possible!'
            print(f"Reminder: {reminder} {customized}")
        else:
            print(f'Reminder: {reminder}')

    case "medium":
        reminder = (f"'{task}' is a medium priority task.")
        if time_bound == 'yes':
            customized = 'Do it before the day is done.'
            print(f'Reminder: {reminder} {customized} ')
        elif time_bound != 'yes':
            customized = "Remember to finish it before it's too late."
            print(f"Reminder: {reminder} {customized} ")
        else:
            print(f'Reminder: {reminder}')

    case "low":
        reminder = (f"'{task}' is a low priority task.") 
        if time_bound == 'yes':
            customized = 'Allocate time to finish it when you can.'
            print(f'Reminder: {reminder} {customized} ')
        else:
            print(f'Reminder: {reminder}')

    case _:
        reminder = 'Priority is invalid.'
        print (f' Reminder: {reminder}')






