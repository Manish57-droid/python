#Python code to find day at which a particular date occurs

import calendar

def isleap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0:
            return True
        else:
            return False

def valid_dates(d,m,y,l):
    #if it is leap year
    if l:
        if m==2:
            if d<30:
                return True
            else:
                return False
        #for months until July
        elif m<8:
            if m%2==0:
                if d<31:
                    return True
                else:
                    return False
            else:
                if d<32:
                    return True
                else:
                    return False
        #for months onwards August
        else:
            #even months
            if m%2==0:
                if d<32:
                    return True
                else:
                    return False
            else:
                if d<31:
                    return True
                else:
                    return False
    else:
        if m==2:
            if d<30:
                return True
            else:
                return False
        #for months until July
        elif m<8:
            if m%2==0:
                if d<31:
                    return True
                else:
                    return False
            else:
                if d<32:
                    return True
                else:
                    return False
        #for months onwards August
        else:
            #even months
            if m%2==0:
                if d<32:
                    return True
                else:
                    return False
            else:
                if d<31:
                    return True
                else:
                    return False

def get_day(day_index):
    days_of_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return days_of_week[day_index]

#inputting year
while(1):
    year = int(input("Enter year: "))
    if year<1970:
        print("Enter years only after 1970.")
    else:
        break

leap = isleap(year)

#inputting month
while(1):
    month = int(input("Enter month: "))
    if month>0 and month<13:
        break
    else:
        print("Enter correct month number.")
        
#inputting date
while(1):
    date = int(input("Enter date: "))
    if date>0 and valid_dates(date,month,year,leap):
        break
    else:
        print("Enter valid date.")

day_index = calendar.weekday(year,month,date)
day = get_day(day_index)

#final output
print(date,"/",month,"/",year,"lies on",day)