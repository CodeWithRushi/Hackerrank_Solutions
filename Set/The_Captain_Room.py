size=input()
set_A,set_B=set(),set()
for room in (input().split()):
    if room not in set_A:
        set_A.add(room)
    else:
        set_B.add(room)
set_A.difference_update(set_B)
print(set_A.pop())