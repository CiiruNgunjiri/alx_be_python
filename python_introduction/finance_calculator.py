# python script to calculate user's motnhly savings based on inputted monthly income and expenses.
# prompt the user for their monthly income and monthly expenses

monthly_income = input ("Enter your monthly income:")
monthly_expenses = input ("Enter your total monthly expenses:")

# calculate the monthly savings after expenses

monthly_savings = int(monthly_income) - int(monthly_expenses)

# assign the variable 'interest' a fixed value of 5% annually
# calculate the projected savings after one year, adding the interest.

interest = 0.05
annual = 12

projected_savings = (monthly_savings * annual + (monthly_savings * annual * interest))

print (monthly_savings)
print (projected_savings)

