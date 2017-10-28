n = int(raw_input())
s = set(map(int, raw_input().split())) 
n1 = int(raw_input())
for i in range(n1):
    cmd=raw_input().split()
    if cmd[0]=="remove":
        s.remove(int(cmd[1]))
    if cmd[0]=="discard":
        s.discard(int(cmd[1]))
    if cmd[0]=="pop":
        s.pop()
print sum(s)