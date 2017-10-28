# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N= int(raw_input())
Orddic = OrderedDict()
for _ in range(N):
    CM= raw_input().rpartition(" ")
    if CM[0]  in Orddic.keys() :
        Orddic[CM[0]] = int(Orddic.get(CM[0])) + int(CM[2]) #if the meal is already in the dictionary sum with the new one
    else:
        Orddic[CM[0]] = (CM[2]) #or just add it
for k,v in Orddic.items():
    print k, v