def safe_divide(numerator, denominator):
    # robust_division_calculator.py

   try:
        # Attempt to convert inputs to floats
      num = float(numerator)
      denom = float(denominator)
        
        # Perform division
      result = num / denom
      return f"The result of the division is {result}"
    
   except ZeroDivisionError: #number cannot be divided by zero
      return "Error: Cannot divide by zero."
    
   except ValueError: #operation cannot run without proper data type(float/integer)
      return "Error: Please enter numeric values only."

   
   
      
