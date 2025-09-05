studentrecord=[]
studentinfo={}

for n in range(0,2):
    studentinfo={}
    studentinfo["id"]=int(input("please enter student id : "))
    studentinfo["name"]=input("please enter student name : ")
    studentinfo["address"]=input("please enter your address : ")
    studentrecord.append(studentinfo)
    
    

print("please enter 1 for searching id ")
print("please enter 2 for searching name ")
print("please enter 3 for searching address ")
choice=int(input("please enter yur choice :"))

if choice==1:
    search=int(input("please enter your id"))
    for n in studentrecord:
        if n["id"]==search:
            flag=1
    if flag==1:
        print("id found")  
    else:
        print("id not found")       
elif choice==2:
    search=input("please enter your name")
    for n in studentrecord:
        if n["name"]==search:
            flag=1
    if flag==1:
        print("name found")
    else:
        print("name not found")

          
elif  choice==3:
    search=input("please enter your address")
    for n in studentrecord:
        if n["address"]==search:
            flag=1
    if flag==1:
        print("address found")
    else:
        print("address not found")        
else:
    print("enter valid option")



    