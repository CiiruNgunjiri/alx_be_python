def safe_divide(numerator, denominator):

 # Convert inputs to float (or int) to ensure they are numeric
   try:
        numerator = float(numerator)  # Convert numerator to float
        denominator = float(denominator)  # Convert denominator to float

   except ValueError:
        
        raise ValueError("Error: Please enter numeric values only.")
      
#raise an error if denominator is equal to 0
   if denominator == 0:

      raise ZeroDivisionError ("Error: Cannot divide by zero.")
   
   return numerator / denominator

     
try:
   numerator = input('Enter numerator: ')
   denominator = input('Enter denominator: ')
    
   result = safe_divide(numerator, denominator)

   print(f"The result of the division is " f'{result:.1f}')
except ZeroDivisionError as e:
   print(f"Error: {e}")  # Handle division by zero
except ValueError as ve:
   print(f"Error: {ve}")  # Handle non-numeric input errors
