if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    ar = []
    p = 0
    for i in range ( x + 1 ) :
         for j in range( y + 1):
                for h in range(z+1):
                     if i+j+h != n:
                        ar.append([])
                        ar[p] = [ i , j, h]
                        p+=1
print ar 