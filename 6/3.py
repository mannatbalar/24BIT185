# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Function to get the number of days in a given month
def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28

# Function to count the total days from a date to the start of that year
def days_from_start_of_year(day, month, year):
    days = day
    for m in range(1, month):
        days += days_in_month(m, year)
    return days

# Function to calculate the number of days between two dates
def days_between_dates(date1, date2):
    d1, m1, y1 = date1
    d2, m2, y2 = date2

    total_days = 0

    # If the years are the same, count days within the same year
    if y1 == y2:
        return abs(days_from_start_of_year(d2, m2, y2) - days_from_start_of_year(d1, m1, y1))

    # Count days from the first date to the end of its year
    total_days += (365 + is_leap_year(y1)) - days_from_start_of_year(d1, m1, y1)
    
    # Count days in the years between
    for year in range(y1 + 1, y2):
        total_days += 365 + is_leap_year(year)
    
    # Count days from the start of the second date's year to its date
    total_days += days_from_start_of_year(d2, m2, y2)
    
    return total_days

# Example dates
date1 = (12, 4, 2023)
date2 = (22, 4, 2025)

# Calculate difference
days_difference = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {days_difference} days")