# prompt the user to input their current age with a question
# display the age written by user

user = input("How old are you?")

print(user)

# calculate the age of the user in 2050 assuming current year is 2023
# determine variables and assign values

current_age = user
current_year = 2023
future_year = 2050

age = int(current_age) + (future_year - current_year)

# print the user's age in 2050 in the format: In 2050, you will be [age] years old

print (f"In {future_year}, you will be {age} years old.")



