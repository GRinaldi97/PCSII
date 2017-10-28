from collections import OrderedDict
def merge_the_tools(string, k):
    L=[]
    for i in range(0,len(string), k):
        L.append(string[i:i+k])
    for x in L:
        print "".join(OrderedDict.fromkeys(x))