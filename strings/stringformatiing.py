def print_formatted(number):
    L=[]
    for x in range(1, number+1):
             L.append(format(x,"b"))
    w=len(str(L[-1]))
    for i in range(1, number+1):
            print str(i).rjust(w), format(i,'o').rjust(w),format(i,"2X").rjust(w), format(i,"b").rjust(w)