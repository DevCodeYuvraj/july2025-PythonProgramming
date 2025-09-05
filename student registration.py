
flag=0
def menu():
    print("1. for student registration")
    print("2 . for view student record")
    print("3. for search student data")
    print("4. for exit")
    print("5. for delete student record")
    print("please enter your choice :")
    output=input()
    return output
def registration():
    studentrecord={}
    studentrecord["id"]=input("please enter student id : ")
    studentrecord["name"]=input("please enter student name : ")
    studentrecord["address"]=input("please enter student address : ")
    listofstudent.append(studentrecord)

def viewstudentdata():
    print(listofstudent)
    
def search():
    search=input("enter id you want to search : ")

    for n in listofstudent:
        if n["id"]==search:
            flag=1
        if flag==1:
            print("******record found*******")
            print(n)
    
def delete():
    delete=input("please enter record id you want to delete: ")
    for n in listofstudent:
        if delete==n["id"]:
            listofstudent.remove(n)
            print("record deleted successfully")   
                 
listofstudent=[]
while(True):
    option=int(menu())
    if option==1:
        registration()
    elif option==2:
        viewstudentdata()
    elif option==3:
        search()
    elif option==4:
        break 
    elif option==5:
        delete()
    else:
        print("enter valid option")               