from collections import  Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
Number= int(raw_input())
ListWords = [raw_input().strip() for _ in range(Number)]
OrdCount =OrderedCounter(ListWords).values()
print len(set(ListWords))
for x in OrdCount:
    print x,