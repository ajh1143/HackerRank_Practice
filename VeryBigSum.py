#!/bin/python3

import os
import sys

def aVeryBigSum(n, ar):
    summer = 0
    for each in range(n):
        summer+=ar[each]
    return summer

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(n, ar)
    f.write(str(result) + '\n')
    f.close()
