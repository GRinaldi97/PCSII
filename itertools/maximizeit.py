from itertools import product
A=map(int,raw_input().split())
L=[]
for _ in range(int(A[0])):
    L.append([x**2 for x in map(int, raw_input().split()[1:])])
Pr= list(product(*L))
print max(sum(x)%A[1] for x in Pr)