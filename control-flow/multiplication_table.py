#generate and print the multiplication for a given number

user = input('Enter a number to see its multiplication table: ')

number = int(user)

#the for loop iterates through the designated range
for i in range(1, 11): #range to be used within the multiplication table
    product = (number * i)
    print (f'{number} * {i} = {product}')
