#Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. 
#Print the decimal value of each fraction on a new line.

#!/bin/python3

import os
import sys

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for each in arr:
        if each < 0 :
            neg += 1
        elif each > 0:
            pos += 1
        else:
            zer += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))
    return None 
    
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
