x,y=map(int, input().split())
choice=int(input())
if choice==1:
    print(x+y)
elif choice==2:
    print(x-y)
elif choice==3:
    print(x*y)
elif choice==4:
    print(x/y)
    print(x//y)
else:
    print("invalid choice")
