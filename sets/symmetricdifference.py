# Enter your code here. Read input from STDIN. Print output to STDOUT
a=raw_input().split()
b=set(map(int,raw_input().split()))
c=raw_input().split()
d=set(map(int,raw_input().split()))
j = sorted(b.symmetric_difference(d))
for x in j:
    print x