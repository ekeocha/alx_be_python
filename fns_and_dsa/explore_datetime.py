from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    days = int(input("Enter number of days to add: "))
    future_date = datetime.now() + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Function calls
display_current_datetime()
calculate_future_date()
