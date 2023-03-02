#calculator
while True: 
    x,y=map(int, input("enter two numbers ").split())
    print("1.addition\n2.substraction\n3.multiply\n4.divide")
    choice=int(input("enter the operation you want to perform"))
    f=open("history.txt","w")
    if choice==1:
        a=x+y
        print(a)
        f.write(str(a))
    elif choice==2:
        a=x-y
        print(a)
        f.write(str(a))
    elif choice==3:
        a=x*y
        print(a)
        f.write(str(a))
    elif choice==4:
        a=x/y
        print(a)
        f.write(str(a))
    else:
        print("invalid choice")
        break
    if input("continue ?").lower()=="no":
        break
    f.close()
    

'''
#list examples
A=[34,56,12]
print(A)
A.append(100) #to add 100 at the end of the list
print(A)
A.insert(2,200) #to add 200 at index 2
print(A)
#to update
A[3]=120
print(A)
#to delete
A.pop() #to remove last element from the list
print(A)
A.remove(200) # to remove specific element
print(A)
A.clear() #to clear all elements from the list
print(A)
del A #to clear the list from the memory
#print(A)
A=[34,56,89,12,78]
print(len(A))
print(sum(A))
print(max(A))
print(min(A))

#tuple examples
days=('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
print(type(days))
print(days[3])
print(days[2:])
print(days[:3])
print('friday' in days)
print('holiday' in days)
print(days.index('friday'))
print(days.count('friday'))
del days

#dictionary examples
qbank={1:{"quest":"2^3","opt":[3,4,8,9],"cans":"8"}}
print(qbank)
print(qbank[1]["quest"])
print(qbank[1]["opt"])
print(qbank[1]["cans"])






'''
