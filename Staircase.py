#Write a program that prints a staircase of n size 
#Create a staircase built with hashes and spaces, whose width and height are both equal to n 
#and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
"""
Ex. Output of n == 6
     # 
    ##
   ###
  ####
 #####
######
""" 

#!/bin/python3

import os
import sys

def staircase(n):
    spaces = " "
    hashes = "#"
    for x in range(n):
        print((n-x-1)*spaces + ((x+1)*hashes))
    return None 

if __name__ == '__main__':
    n = int(input())

    staircase(n)
