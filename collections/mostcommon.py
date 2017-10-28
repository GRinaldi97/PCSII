#!/bin/python
from collections import Counter
if __name__ == "__main__":
    s = list(raw_input().strip())
    e = (Counter(s).most_common(3)) 
    d= {}
    for x in e:
        d[x[0]]= x[1]
    sort=[v for v in sorted(d.iteritems(), key=lambda(k,v): (-v,k))] #this command sorts the element first by value and the by the key 
    # i've used -v so that it sorts in descending order by value and than by key
    for y in sort:
        print y[0], y[1]