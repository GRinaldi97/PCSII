# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
for k,g in groupby((raw_input()), int):
    print (len(list(g)),k),