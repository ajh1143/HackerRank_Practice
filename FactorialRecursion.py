'''
Write a factorial function that takes a positive integer, N as a parameter and prints the result of N!N(factorial)
'''
#!/bin/python3

import sys

def factorial(n):
    if n <= 1 :
        return 1
    else:
        newN = n*factorial(n-1)
        return newN

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
