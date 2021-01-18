Number=int(input())

Elements= set(map(int,input().split()))

Commands_Count=int(input())

for i in range(Commands_Count) :

    choice=input().split()
    if choice[0]=="pop" :
        Elements.pop()
    elif choice[0]=="remove" :
        Elements.remove(int(choice[1]))
    elif choice[0]=="discard" :
        Elements.discard(int(choice[1]))
print (sum(Elements))