# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N= int(raw_input())
L=[]
P=[]
for x in range(N+1):
    cm= raw_input().split()
    L.append(cm)
cm = L[0].index('MARKS') #i've added to a L list all the rows of the input so if I know the index regarding the mark I know the position of every mark
for x in L[1:]:  
    P.append(int(x[cm]))
print "{0:.2f}".format(float(sum(P))/len(P))