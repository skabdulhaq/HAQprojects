def leap_year_not(year):
    a = year % 4
    b = year % 100
    c = year % 400
    if a == 0:
        if b == 0:
            if c == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = ['31', '28', '31', '30', '31', '31', '30', '31', '30', '31', '30', '31']
    is_leap = leap_year_not(year)
    if month > 12 or month < 1:
        return "Invalid Month"
    if is_leap == True and month == 1:
        return 29
    else:
        return month_days[month-1]


year = int(input("Please Enter Year => "))
month = int(input("Enter A Month => "))
days = days_in_month(year, month)
