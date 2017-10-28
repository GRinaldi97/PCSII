from collections import deque
if __name__ == '__main__':
    N = int(raw_input())
    L=deque()
    for i in range(0,N):
        cmd=raw_input().split();
        if cmd[0] == "append":
                L.append(cmd[1])
        elif cmd[0] == "appendleft":
              L.appendleft(int(cmd[1]))
        elif cmd[0] == "pop":
             L.pop();
        elif cmd[0] == "popleft":
             L.popleft()
for x in L:
    print int(x),