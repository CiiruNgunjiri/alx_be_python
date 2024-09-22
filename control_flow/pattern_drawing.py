#using nested loops to print a square pattern

#enter a positive integer 
user = int(input('Enter the size of the pattern: '))

pattern = user

#check if input is a positive integer
while pattern <= 0:
    print('Please enter a positive integer!')
    break

#use nested loops to draw pattern
row = 0
while row < pattern:
    column = 0
    while column < pattern:
        print ('*', end='')
        column += 1
    print()
    row += 1
    
