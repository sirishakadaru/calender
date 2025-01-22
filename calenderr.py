def is_leap_year(year):
    """
    Determine if a year is a leap year.
    :param year: The year to check.
    :return: True if leap year, False otherwise.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def get_first_day_of_month(year, month):
    """
    Calculate the first day of the given month and year.
    :param year: The year as an integer.
    :param month: The month as an integer (1 for January, 12 for December).
    :return: The index of the first day (0 = Sunday, 6 = Saturday).
    """
    
    if month in [1, 2]:  
        year -= 1
        month += 12
    k = year % 100
    j = year // 100
    first_day = (1 + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7
    return (first_day + 6) % 7  

def get_days_in_month(year, month):
    """
    Return the number of days in a given month and The year as an integer.
    :param month: The month as an integer.
    :return: Number of days in the month.
    """
    if month in [4, 6, 9, 11]:  
        return 30
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    return 31  # All other months

def print_calendar(year, month):
    """
    Print the calendar for a given month and year.
    :param year: The year as an integer.
    :param month: The month as an integer.
    """
    
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    
    month_name = month_names[month - 1]
    days_in_month = get_days_in_month(year, month)
    first_day = get_first_day_of_month(year, month)
    
    
    print(f"{month_name} {year}".center(28))
    print("Sun Mon Tue Wed Thu Fri Sat")
    
    
    print("    " * first_day, end="")

    
    current_day = 1
    while current_day <= days_in_month:
        print(f"{current_day:>3} ", end="")
        if (first_day + current_day) % 7 == 0:  
            print()
        current_day += 1
    print()  
try:
    
    month_name_input = input("Enter Month Name (full or abbreviated): ").strip().capitalize()
    year = int(input("Enter Year: "))
    

    month_mapping = {
        "January": 1, "Jan": 1,
        "February": 2, "Feb": 2,
        "March": 3, "Mar": 3,
        "April": 4, "Apr": 4,
        "May": 5,
        "June": 6, "Jun": 6,
        "July": 7, "Jul": 7,
        "August": 8, "Aug": 8,
        "September": 9, "Sep": 9,
        "October": 10, "Oct": 10,
        "November": 11, "Nov": 11,
        "December": 12, "Dec": 12
    }
    
    
    if month_name_input not in month_mapping:
        raise ValueError("Invalid month name or abbreviation. Please enter a valid month.")
    
    month = month_mapping[month_name_input]
    
    
    print_calendar(year, month)
except ValueError as e:
    print(f"Error: {e}")
