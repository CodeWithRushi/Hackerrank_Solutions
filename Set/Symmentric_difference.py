

"""
#Introduction of sets

def average(array):
    size=len(set(array))
    total=sum(set(array))
    avg=(total/size)
    return avg    # your code goes here
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
"""
"""
#Symmentric Difference

first=int(input())
second=set(map(int,input().split()))
third=int(input())
fourth=set(map(int,input().split()))

result=sorted(second.symmetric_difference(fourth))
for i in result:
    print(i)
"""


"""
#No_Idea

N,M = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
#Union set A & B
C = A | B
#Exclude all numbers which doesn't exit in both A & B
N = (i for i in N if i in C)
#Add 1 if number is in set A else subtract 1
print(sum(1 if i in A else -1 for i in N ))

"""


