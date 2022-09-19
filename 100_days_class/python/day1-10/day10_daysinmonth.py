month_dict = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11,
    "dec": 12
    }


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# Doc strings in use!


def days_in_month(year, month):
    """Returns the number of days in inputed month"""
    if year == '' or month == '':
        return "One of the inputs is blank"
    elif is_leap(year) is True:
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in = (month_dict[month] - 1)
    days = (month_days[days_in])
    return days


#Do NOT change any of the code below
year = int(input("Enter a year: "))
month = input("Enter a month: ")
days = days_in_month(year, month)
print(days)
