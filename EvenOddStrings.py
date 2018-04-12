#Given a string S, of length N,  print its even-indexed and odd-indexed characters as space-separated strings on a single line
#Note: 0 is considered to be an even index.

#Define Number Lines to accept/print as N
N = int(input())
#Create list to hold each string
strings = []
#Set For-Loop to capture N-number of string inputs
for entry in range(N):
    #Add input string to strings list
    strings.append(input())
#Set For-Loop to slice list elements using even/odd patterns
for string in strings:
    #Capture even/odd array via slice
    outputEven = [string[0::2]]
    outputOdd = [string[1::2]]
    #Merge the arrays
    outputCombine = outputEven+outputOdd
    #Join the arrays seperated by a space
    outputCombo = " ".join(outputCombine)
    #Print the arrays as strings
    print(outputCombo)
