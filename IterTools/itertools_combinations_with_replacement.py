from itertools import combinations_with_replacement
string,size=input().split()
k=list(combinations_with_replacement(sorted(string),int(size)))
for i in k:
	print(''.join(i))