#Compare values in equal positions of two arrays, awarding a point to the array with the greater value in the comparison point.
#If values are equal, no points will be awarded for that comparison.
#Return a list of values indicating the score for each array owner, named Alice and Bob

#!/bin/python3

import os
import sys

def solve(a0, a1, a2, b0, b1, b2):
    aliceScore = 0
    bobScore = 0
    alice = [a0, a1, a2]
    bob = [b0, b1, b2]
    for t in range(3):
        if alice[t] == bob[t]:
            pass
        elif alice[t] > bob[t]:
            aliceScore +=1
        else:
            bobScore += 1    
    return aliceScore, bobScore
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    a0A1A2 = input().split()
    a0 = int(a0A1A2[0])
    a1 = int(a0A1A2[1])
    a2 = int(a0A1A2[2])
    b0B1B2 = input().split()
    b0 = int(b0B1B2[0])
    b1 = int(b0B1B2[1])
    b2 = int(b0B1B2[2])
    result = solve(a0, a1, a2, b0, b1, b2)
    f.write(' '.join(map(str, result)))
    f.write('\n')
    f.close()
