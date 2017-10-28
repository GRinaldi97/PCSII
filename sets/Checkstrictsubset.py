A= set(raw_input().split())
N= int(raw_input())
L=[]
for _ in range(N):
    CM= set(raw_input().split())
    L.append(CM)
print all((item).issubset(A) for item in L)