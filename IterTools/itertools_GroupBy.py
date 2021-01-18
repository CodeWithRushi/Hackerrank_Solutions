from itertools import groupby 
number=input()
for key,group in groupby(number):
    print((len([*group]),int(key)),end='')