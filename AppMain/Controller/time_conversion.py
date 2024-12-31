import datetime
from datetime import datetime
import os
import sys
import re 
import random

def timeConversion(s):
    time = int(s)
    hh = int(time[:2])
    mm = time[3:5]
    ss = time[6:8]
    period = time

    if period == "AM":
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12
    
    result = f"{hh:02}:{mm}:{ss}"
    return result

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
