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
    

#part 2
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

#part 3
f=open("sid.txt","w") #w..to create a new file and allow to write in the file
f.write("Two")
f.close()
print("File created")

f=open("sid.txt","w")
while True:
    txt=input("Enter text")
    if txt=='end':
        break
    f.write(txt+"\n")
f.close()


# 'r' mode
f=open("sid.txt","r") #r...to read the file
st=f.read()
print(st)
print(type(st))

# 'a' mode
f=open("sid.txt","a") #to add records in existing file
f.write("DBMS\n")
f.write("UNIX\n")
f.close()



#examples
#wap to store roll no,name and marks of p,c,m in a file with name
#'stud.txt'
f=open('stud.txt','w')
while True:
    rno=input("Roll no?")
    nm=input("Name?")
    p=input("Physics marks?")
    c=input("Chemistry marks?")
    m=input("Math marks?")
    rec=rno+","+nm+","+p+","+c+","+m+"\n"
    f.write(rec)
    if input("Continue?")=='no':
        break
f.close()
print("File created")
f=open('stud.txt','r')
st=f.readlines()
f.close()
#print(st)
student=[]
for rec in st:
    each_stud=rec.split(",")
    #print(each_stud)
    each_stud[2]=int(each_stud[2])
    each_stud[3]=int(each_stud[3])
    each_stud[4]=int(each_stud[4][:-1])
    #print(each_stud)
    student.append(each_stud)
print(student)
for S in student:
    tot=S[2]+S[3]+S[4]
    per=tot/3
    if S[2]>=35 and S[3]>=35 and S[4]>=35:
        rem='Pass'
        if per>=60:
            grade='A'
        elif per>=45:
            grade='B'
        else:
            grade='C'
    else:
        rem='Fail'
        grade='-'
    print("Roll No:",S[0])
    print("Name:",S[1])
    print("Marks:")
    print("Physics\tChemistry\tMaths")
    print(S[2],"\t",S[3],"\t","\t",S[4])
    print("Total:",tot,"\tPercentage:",per)
    print("Remark:",rem,"\tGrade:",grade)







