from itertools import combinations_with_replacement
word,K= raw_input().split(" ")
L=[]
for t in list(combinations_with_replacement(word,int(K))):
           L.append(sorted(t))
L= sorted(sorted(L), key=len)
for x in L:
    print "".join(x)