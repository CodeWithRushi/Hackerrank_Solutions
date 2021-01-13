from itertools import combinations

string,size=input().split()


for i in range(1,int(size)+1):  
	
	for j in list(combinations(sorted(string),i)):
		print(''.join(j))