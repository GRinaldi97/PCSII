# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
word, K= raw_input().split(" ")
for x in sorted(list(permutations(str(word), int(K)))):
        print "".join(x)