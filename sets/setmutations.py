if __name__ == '__main__':
    N = int(raw_input())
    T=set(map(int,(raw_input().split())))
    H=int(raw_input())
    L=[]
    for i in range(H*2):
        cmd=(raw_input().split())
        L.append(cmd)
    for x in range(len(L)):
            if L[x][0]=="intersection_update":
                T.intersection_update(map(int,L[x+1]))
            if L[x][0]=="update":
                T.update(map(int,L[x+1]))
            if L[x][0]=="symmetric_difference_update":
                T.symmetric_difference_update(map(int,L[x+1]))
            if L[x][0]=="difference_update":
                T.difference_update(map(int,L[x+1]))
    print sum(T)