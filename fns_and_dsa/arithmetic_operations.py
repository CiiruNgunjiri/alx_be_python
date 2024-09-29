def perform_operation(num1 , num2, operation) -> float:
  num1 = float(num1)
  num2 = float(num2)
  operation = str(operation)
  """
  Performs basic arithmetic operations based on the provided parameters.

  Args:
      num1: The first number (float).
      num2: The second number (float).
      operation: The operation to perform ("add", "subtract", "multiply", or "divide").

  Returns:
      The result of the arithmetic operation (float) or a message for division by zero.
  """
  operation = operation.lower()  # Ensure case-insensitive operation handling
  if operation == "add":
    return num1 + num2
  elif operation == "subtract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    if num2 == 0:
      return "Error: Cannot divide by zero."
    else:
      return num1 / num2
  else:
    return "Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."
 