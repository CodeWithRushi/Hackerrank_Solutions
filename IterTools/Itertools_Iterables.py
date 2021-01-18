from itertools import combinations
length=int(input())
alphabet=input().split()
size=int(input())

lists=list(combinations(alphabet,size))
Filter=list(filter(lambda x:'a'in x,lists))
print(len(Filter)/len(lists))
from itertools import combinations
length=int(input())
alphabet=input().split()
size=int(input())

lists=list(combinations(alphabet,size))
Filter=list(filter(lambda x:'a'in x,lists))
print(len(Filter)/len(lists))
