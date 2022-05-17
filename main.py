#!/bin/python3

import time as t
import sys

minutes = 30 # default is 30 min
secondsInMinute = 60

def countDown(m):   
    #calculate total seconds
    totalSec = m*secondsInMinute

    for i in range(totalSec):
        print (f"{totalSec-i} ... seconds remaining \n")
        t.sleep(1)

#we ask only for minutes
if len(sys.argv) < 0:
    minutes = int(input("How many minutes ")) 
if len(sys.argv) > 1:
    minutes = int(sys.argv[1])



countDown(minutes) #devide imput by seconds
print(f"time is up")


#todo
# now it gives an ugly 1200 seconds remain for 20 min
# turn this into a nice count down of 20:00