from collections import Counter
X=int(input())
Sizes=Counter(map(int,input().split()))
sum=0
N=int(input())
for i in range(N):
	size,price=map(int,input().split())
	if Sizes[size]:
		sum+=price
		Sizes[size]-=1
print(sum)
		