def safe_divide(numerator, denominator):

 # Convert inputs to float (or int) to ensure they are numeric
   try:
        numerator = float(numerator)  # Convert numerator to float
        denominator = float(denominator)  # Convert denominator to float

   except ValueError:
        
        raise ValueError("Both numerator and denominator must be numeric values.")
      
#raise an error if denominator is equal to 0
   if denominator == 0:

      raise ZeroDivisionError ("the denominator cannot be zero")
  
   else:
  
      return numerator / denominator
     
try:
   numerator = input('Enter numerator: ')
   denominator = input('Enter denominator: ')
    
   result = safe_divide(numerator, denominator)
   print(f"Result: {result}")
except ZeroDivisionError as e:
   print(f"Error: {e}")  # Handle division by zero
except ValueError as ve:
   print(f"Value Error: {ve}")  # Handle non-numeric input errors
