from collections import OrderedDict
od=OrderedDict()
quentity=int(input())
for i in range(quentity):
    str=input().split()
    value=int(str[-1])
    key=' '.join(str[:-1])
    if key in od:
        od[key]=od[key]+value
    else:
        od[key]=value


for key,value in od.items():
    print(key,value)