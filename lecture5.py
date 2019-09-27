#File space algorithm

##import needed modules
##define a funtion that takes a dir
##    set a total = 0
##    loop over each item in current dir
##    if item is a file
##        add size of item to total
##    else
##        if item is a dir
##            add result of calling funtion on the dir to total
##    return total
##
##main
##ask user for a dir
##call funtion on use dir
##print results 

##import datetime
##
##now = datetime.date.today()
##birthday = datetime.date.today()
##bday = datetime.date(1999, 10, 28)
##age = now - bday
##
##print("I am", age.days, "days old.")
##print("Which is", age.days / 365, "years")
##
##import time
##start = time.clock()
##for i in range (300):
##    print(i)
##end = time.clock()
##print("\nTotal time: ", end - start, "seconds")

import datetime
import random
import time

while True:
    start = time.clock()
    month = random.randrange(1,13)
    day = random.randrange(1,32)
    year = random.randrange(1900,2020)
    
    try:
        now = datetime.date(year, month, day)
        print(now.strftime("%d %b %Y is a %A on the %d day of %B"))
    except:
        print("Not valid")
    else:
        if now.strftime("%A") == "Thursday" and now.strftime("%B") == "Feburary" and now.strftime("%Y") % 7 == 0:
            end = time.clock()
            print("\nTotal time: ", end - start, "seconds")
