from itertools import permutations

string,size=input().split()
new_list=sorted(list(permutations(string,int(size))))
res = list(map(" ".join, new_list)) 
for i in res:
	print(i)