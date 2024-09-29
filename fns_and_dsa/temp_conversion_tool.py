# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

FAHRENHEIT_TO_CELSIUS_FACTOR = FAHRENHEIT_TO_CELSIUS_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = CELSIUS_TO_FAHRENHEIT_FACTOR

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius using the global conversion factor.
    
    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.
        
    Returns:
    loat: Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit using the global conversion factor.
    
    Parameters:
        celsius (float): Temperature in Celsius.
        
    Returns:
        float: Temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # User Input
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
