# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
Number= int(raw_input())
ListElem= raw_input().split()
P= int(raw_input())
L=range(1, Number+1)
H=[]
T=[]
counter=0
for x in list(combinations(L,P)): #gives all the combinations of L of length P and I append the tuples to H
    H.append(x)
for i in (i for i,x in enumerate(ListElem) if x == "a"): #for each element of the list that is "a" appends to T the index (1based)
         T.append(i+1)
for x in H:   #for each element of the H list(made by tuples) if there is any index of a the counter grows by 1
      if any(i in x for i in T ):
                 counter+=1
print (float(counter)/len(H))  