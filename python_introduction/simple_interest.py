# python script that calculates the simple interest earned on an investment
# the formula for simple interest is (I = P * R * T)
# (I) is the interest earned
# (P) is the principal amount (inital investment)
# (R) is the annual interest rate (as a decimal)
# (T) is the time the money is invested for in years

# assign the variables some values
# principal with a value of 1000 representing $1000
# rate with a value of 0.05 representing 5% annual interest rate
# time with a value of 3 representing 3 years

principle = 1000
rate = 0.05
time = 3

interest = principle * rate * time

# print the calculated interest in the format: The simple interest is: [interest]

print (f'The simple interest is: {float(interest)}')



