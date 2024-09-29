#Provided main.py for Testing:

from arithmetic_operations import perform_operation
"""assign values to variables found within the function perform_operation"""

def main():
    print("Arithmetic Operations")
#convert the input from string to float
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
    