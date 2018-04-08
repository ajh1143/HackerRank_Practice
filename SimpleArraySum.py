#Given an array of integers, find the sum of its elements.
#The first line contains an integer, denoting the size of the array. 
#The second line contains space-separated integers representing the array's elements.

#!/bin/python3

import os
import sys

def simpleArraySum(ar):
     x=0
     for each in ar:
        x += each
     return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simpleArraySum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
