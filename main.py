#!/bin/python3

import time as t

#asking user to give amount of seconds
seconds = int(input("How many seconds to wait "))

for i in range(seconds):
    print (f"{seconds-i} ... seconds remaining \n")
    t.sleep(1)

print(f"time is up")