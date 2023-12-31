from datetime import datetime

def CheckingDate(date_to_check):
    # Get the current date
    current_date = datetime.now().date()

    # Parse the input date
    parsed_date = datetime.strptime(date_to_check, '%Y-%m-%d').date()

    # Calculate the difference in days
    days_difference = (parsed_date - current_date).days

    # Check if the difference is within the desired range 
    return abs(days_difference) <= 5   #change # if want dif range
