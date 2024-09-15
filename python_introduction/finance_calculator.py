# python script to calculate user's motnhly savings based on inputted monthly income and expenses.
# prompt the user for their monthly income and monthly expenses

monthly_income = input ("Enter your monthly income:")
monthly_expenses = input ("Enter your total monthly expenses:")

# convert the string from the input to float

monthly_income = float(monthly_income)
monthly_expenses = float(monthly_expenses)

# calculate the monthly savings after expenses

monthly_savings = monthly_income - monthly_expenses

# assign the variable 'interest' a fixed value of 5% annually
# calculate the projected savings after one year, adding the interest.

interest = 0.05
annual = 12

projected_savings = (monthly_savings * annual + (monthly_savings * annual * interest))

print (monthly_savings)
print (projected_savings)

