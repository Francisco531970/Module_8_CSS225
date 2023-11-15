# Francisco Sanchez
# 11/15/23

def is_leap_year(year):
    # Check if the year is evenly divisible by 4
    if year % 4 == 0:
        # Check if the year is evenly divisible by 100
        if year % 100 == 0:
            # Check if the year is evenly divisible by 400
            if year % 400 == 0:
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year
    else:
        return False  # Not a leap year


# Example usage:
year_to_check = 2024
result = is_leap_year(year_to_check)

# Print the result
if result:
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
