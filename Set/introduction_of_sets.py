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

first=int(input())
second=set(map(int,input().split()))
third=int(input())
fourth=set(map(int,input().split()))

result=second.symmetric_difference(fourth)
for i in result:
    print(i)

