from collections import namedtuple
Total_Students=int(input())
Element=input().split()
Columns = namedtuple('Columns',Element)
l=[int(Columns._make(input().split()).MARKS) for i in range(Total_Students)]
print(sum(l)/Total_Students)