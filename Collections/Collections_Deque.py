from collections import deque
d = deque()
No_Of_Operations=int(input())
for i in range(No_Of_Operations):
    string=input().split()
    
    if string[0]=='append':
        d.append(string[1])
    
    elif string[0]=='appendleft':
        d.appendleft(string[1])
    elif string[0]=='pop':
        d.pop()
    elif string[0]=='popleft':
        d.popleft()


print(*d)