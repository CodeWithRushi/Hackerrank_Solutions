A=input()
Element_A=set(map(int,input().split()))
N=input()

for i in range(int(N)) :

    choice=input().split()
    if choice[0]=="intersection_update" :
        Element_A.intersection_update(set(map(int,input().split())))
    elif choice[0]=="update" :
        Element_A.update(set(map(int,input().split())))
    elif choice[0]=="symmetric_difference_update" :
        Element_A.symmetric_difference_update(set(map(int,input().split())))
    elif choice[0]=="difference_update" :
        Element_A.difference_update(set(map(int,input().split())))

print (sum(Element_A))