#script that prompts the user to do calculations between two numbers using match case

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /): ')

#execute the chosen operation based on the user's input
#print out the result in the format below: 
#print (f'The result is {result}.')

match operation:
    case '+':
        result = num1 + num2
        print(f'The result is {result}.') 
    case '-':
        result = num1 - num2
        print(f'The result is {result}.') 
    case '*':
          result = num1 * num2
          print(f'The result is {result}.') 
    case '/':
        if num2 == 0: #user should not divide by zero
            result = print('Division by zero is not allowed')
        else: 
            result = num1 / num2
            print(f'The result is {result}.') 
    case _:
        result = 'Invalid result'
        print(result)

 
   
 
        
