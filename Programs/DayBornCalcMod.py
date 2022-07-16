import datetime

#Program Logic
def GetDay():
    month = int(input("Enter Month as a Number:    "))
    day = input("Enter Day:    ")
    year = int(input("Enter Year:    "))
    dayStrip = day.lstrip('0')
    birthdate = datetime.date(year, month, int(dayStrip))
    dayWeek = birthdate.weekday()
    if(dayWeek == 0):
        return "Monday"
    elif(dayWeek == 1):
        return "Tuesday"
    elif(dayWeek == 2):
        return "Wednesday"
    elif(dayWeek == 3):
        return "Thursday"
    elif(dayWeek == 4):
        return "Friday"
    elif(dayWeek == 5):
        return "Saturday"
    elif(dayWeek == 6):
        return "Sunday"
