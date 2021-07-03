def isLeapYear(year):
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


print(isLeapYear(20))

def daysInMonth(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month>12 and month<1:
        return "Enter Valid Month"
    elif month==2 and isLeapYear(year):
        return 29
    else :
        return month_days[month-1]

year = int(input("Enter Year : "))    
month = int(input("Enter Month : "))     

print(daysInMonth(year, month))
