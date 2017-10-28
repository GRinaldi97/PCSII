from collections import deque
n= int(raw_input())
for _ in range(n):
    j=int(raw_input())
    L= deque(map(int, raw_input().split()))
    for x in range(1, j-1):
        if L[x]<=L[x+1] or L[x]<=L[x-1]: 
            result = "Yes"
        else:
            result= "No"
            break
    print result