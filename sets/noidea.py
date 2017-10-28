# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = raw_input().split()
Arr= (raw_input().split())
A= set(raw_input().split())
B= set(raw_input().split())
counter = 0
for x in Arr:
    if x in A:
        counter+=1
    if x in B:
        counter+=(-1)
print counter