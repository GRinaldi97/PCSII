NumberOfShoes= int(raw_input())
ListShoes= map(int, raw_input().split())
A= int(raw_input())
Earned=0
for _ in xrange(A):
    cm=raw_input().split() #takes the number and the price/earn as respectively cm[0] and cm[1]
    if int(cm[0]) in ListShoes:
        Earned+= int(cm[1])
        ListShoes.remove(int(cm[0]))
print Earned