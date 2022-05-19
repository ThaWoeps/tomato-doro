#!/bin/python3

import time as t
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread


minutes = 30 # default is 30 min
secondsInMinute = 60
focus = "Work"

def countDown(m):   
    #calculate total seconds
    totalSec = m*secondsInMinute

    for i in range(totalSec):
        print (f"Focusing on {focus},  remaining time: {totalSec-i}\n")
        t.sleep(1)

if __name__ == "__main__":

    #we ask only for minutes
    if len(sys.argv) < 0:
        minutes = int(input("How many minutes ")) 
    if len(sys.argv) > 1:
        minutes = int(sys.argv[1])
        if len(sys.argv) > 2:
            focus = str(sys.argv[2])

    countDown(minutes) #devide imput by seconds
    print(f"time is up")


#todo
# now it gives an ugly 1200 seconds remain for 20 min
# turn this into a nice count down of 20:00