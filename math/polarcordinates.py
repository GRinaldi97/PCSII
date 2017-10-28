# Enter your code here. Read input from STDIN. Print output to STDOUT
from cmath import phase
S = raw_input()
print abs(complex(S))
print phase(complex(S)) 