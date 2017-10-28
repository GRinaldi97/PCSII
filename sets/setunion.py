# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(raw_input())
A= set(raw_input().split())
b = int(raw_input())
B= set(raw_input().split())
print len(A.union(B))