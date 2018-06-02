def is_leap_year(year):
    is_divisible_by_four = year % 4 == 0
    is_divisible_by_hundred = year % 100 == 0
    is_divisible_by_four_hundred = year % 400 == 0

    if is_divisible_by_four:
        if is_divisible_by_four_hundred:
            return True
        elif is_divisible_by_hundred:
            return False
        else:
            return True
    
    return False
