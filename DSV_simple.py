#Elis Lidberg
#19970325-19005951

def input_year():
    year = 0
    while True:
        try:
            year = int(input('Year: '))
        except ValueError:
            print('Out of allowed range 1583 to 9999')
        else:
            break
    
    if 1583 <= year <= 9999:
        return year
    else:
        print('Out of allowed range 1583 to 9999')
        return input_year()


def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def input_month():
    month = 0
    while True:
        try:
            month = int(input('Month: '))
        except ValueError:
            print('Out of allowed range 1 to 12')
        else:
            break
    
    if 1 <= month <= 12:
        return month
    else:
        print('Out of allowed range 1 to 12')
        return input_month()


def input_day(year, month):
    day = 0
    set_of_2 = {2}
    set_of_30 = {4,6,9,11} 
    set_of_31 = {1,3,5,7,8,10,12}

    if month in set_of_31:
        while True:
            try:
                day = int(input('Day: '))
            except ValueError:
                print('Out of allowed range 1 to 31')
            else:
                break
    
        if 1 <= day <= 31:
            return day
        else:
            print('Out of allowed range 1 to 31')
            return input_day(year, month)
    
    elif month in set_of_30:
        while True:
            try:
                day = int(input('Day: '))
            except ValueError:
                print('Out of allowed range 1 to 30')
            else:
                break
    
        if 1 <= day <= 30:
            return day
        else:
            print('Out of allowed range 1 to 30')
            return input_day(year, month)

    elif month in set_of_2:
        if leap_year(year) == True:
            while True:
                try:
                    day = int(input('Day: '))
                except ValueError:
                    print('Out of allowed range 1 to 29')
                else:
                    break
            if 1 <= day <= 29:
                return day
            else:
                print('Out of allowed range 1 to 29')
                return input_day(year, month)

        else:
            while True:
                try:
                    day = int(input('Day: '))
                except ValueError:
                    print('Out of allowed range 1 to 28')
                else:
                    break
            if 1 <= day <= 28:
                return day
            else:
                print('Out of allowed range 1 to 28')
                return input_day(year, month)


def calculations(year, month, day):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    
    weekday = ( day + 13*(month+1)//5 + year + year//4 - year//100 + year//400 ) % 7

    return weekday

def main():
    year = input_year()
    month = input_month()
    day = input_day(year, month)

    list_of_weekdays = {2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 0: 'Saturday', 1: 'Sunday'}

    weekday = calculations(year, month, day)

    print('\nIt is a ' + list_of_weekdays[weekday])

if __name__ == "__main__":
    main()