# Enter your code here. Read input from STDIN. Print output to STDOUT
K=int(raw_input())
L=map(int,raw_input().split())
A=set(L)
n=sum(L)
n2=sum(A)
print (n2*K-n)/(K-1)