#Amir Afzali
#Counting Sundays Project Euler Question 19

import datetime
#The best way to approach the problem would be to take advantage of the datetime library as it should have all the info I need so import it
def countingsundays():
#Setting up the ranges for month and years
    sundays = sum(1
        for year in range(1901,2001)
            for month in range(1,13)
            if datetime.date(year, month, 1).weekday() == 6)
#for this module sunday is 6 and monday is 0, utilize the module
    return str(sundays)








