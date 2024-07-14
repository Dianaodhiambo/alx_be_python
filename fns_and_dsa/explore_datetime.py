# explore_datetime.py

from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

# Function to calculate the future date
def calculate_future_date(days_to_add):
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

# Main script execution
if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()

    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(days_to_add)
