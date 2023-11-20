import datetime

def get_date_of_birth():
    day = int(input("Napis den sveho narozeni"))
    month = int(input("Napis mesic sveho narozeni"))
    year = int(input("Napis rok sveho narozeni"))

    # Checking if age is legal
    min_age = 0
    max_age = 119
    current_year = datetime.date.today().year
    if current_year - year < min_age and current_year > max_age:
        raise ValueError("Iligal age")

    # Checking if month is legal
    if not month < 1 and not month > 12:
        raise ValueError("Incorrect month of birth")

    # Checking if day is legal
    if day < 1:
        raise ValueError("Day can not be less then 1")
    if month == 2:
        if day > 31:
            raise ValueError("Day can not larger then 31")
    else:
        if day > 30:
            raise ValueError("Day can not larger then 31")

    if month in [7, 8]:
        raise ValueError("You can not be born in July or September")

    return f'{day}.{month}. {year}'


