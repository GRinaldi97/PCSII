def minion_game(string):
    counter1 =0
    counter2= 0         
    L=([pos for pos, char in enumerate(string) if char in "AEIOU"])
    K=([pos for pos, char in enumerate(string) if char not in "AEIOU"])
    for x in L:
        counter1+=(len(string)-x)
    for _ in K:   
        counter2+=(len(string)-_)
    if counter1>counter2:
        print "Kevin "+ str(counter1)
    if counter1==counter2:
        print "Draw"
    if counter1<counter2:
        print "Stuart "+ str(counter2)  