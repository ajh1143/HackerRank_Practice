#Given a square matrix, calculate the absolute difference between the sums of its diagonals (left and right paths)


#!/bin/python3

import os
import sys

def diagonalDifference(a):
    right = [a[i][i] for i in range(len(a))]
    left = [a[i][~i] for i in range(0, len(a))] 
    rightSum = sum(right)
    leftSum = sum(left)
    absDif = abs(rightSum-leftSum)
    return absDif


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)
    f.write(str(result) + '\n')
    f.close()
