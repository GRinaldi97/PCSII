# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A=map(int,(raw_input().split()))
B=map(int,(raw_input().split()))
for x in sorted(list(product(A,B))):
    print x,