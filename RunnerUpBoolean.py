#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given 'n' scores. Store them in a list and find the score of the runner-up.

#Boolean Loop Solution Approach
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arrMax = max(arr)
    while arrMax in arr:
          arr.remove(arrMax)
    print(max(arr))

