Test_Cases=int(input())
for i in range(Test_Cases):
	Size_A=int(input())
	Elements_A=set(map(int,input().split()))
	Size_B=int(input())
	Elements_B=set(map(int,input().split()))
	result=Elements_A.issubset(Elements_B)
	print(result)