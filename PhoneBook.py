''' 
Given N number of names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated 
entry from your phone book on a new line in the form of name=phone number, or "Not found" if the name is not in the dictionary
''' 

import sys 
phoneBook = {}
total = int(input())
for each in range(total):
    pair = input().split(" ")
    key = pair[0]
    value = pair[1]
    phoneBook[key] = value
keyRequests = list(map(str, sys.stdin.read().split()))
for each in keyRequests:
    if each in phoneBook:
        print(each + "=" + phoneBook[each])
    else:
        print("Not found")
