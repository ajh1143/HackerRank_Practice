import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arrMax = sorted(arr)
    arrMin = sorted(arr)
    arrMax.pop(0)
    arrMin.pop(-1)
    return sum(arrMin), sum(arrMax)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    min, max = miniMaxSum(arr)
    print(min, max)
