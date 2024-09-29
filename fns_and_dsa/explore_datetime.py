from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days: int):
    """
    Calculate and display the future date after adding the specified number of days to the current date.

    Parameters:
        days (int): The number of days to add to the current date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Part 1: Display Current Date and Time
    display_current_datetime()
    
    # Part 2: Calculate a Future Date
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

