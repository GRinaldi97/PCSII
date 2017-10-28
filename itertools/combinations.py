from itertools import combinations
word,K= raw_input().split(" ")
L=[]
for k in range(1, int(K)+1):
    for t in list(combinations(word,int(k))):
           L.append(sorted(t))
L= sorted(sorted(L), key=len)
for x in L:
    print "".join(x)