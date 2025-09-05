loginpass={"email":"yuvrajsingh@gmail.com","password":"Bhati@123"}

studentdata=[]

studentinfo={}
update_student_info={}
count=0

print("1. Login")
print("2. signup")
print("3. exit")
menuoption=int(input("please select your choice : "))
while(True):
    if menuoption==1:
        print("\n welcome to login \n")
        userid=input("please enter your user id : " )
        userpassword=input("please enter your password : ")
        if userid==loginpass["email"] and userpassword==loginpass["password"]:
            print("\n login successful \n")
            print("1.  view student information ")
            print("2. edit student information ")
            print("3. exit ")
            userinput=int(input("please enter your choice : "))
            if userinput==1:
                for n in studentdata:
                    count+=1
                    print(studentdata)
                if count<1:
                    print(" \n please signup first\n")
                    menuoption=2
                else:
                    break
            elif userinput==2:
                for n in studentdata:
                    count+=1
                    print(studentdata)
                if count<1:
                    print("\n please signup first ! no data available at this moment :) \n")
                    menuoption=2
                else:
                    print("1. edit student id ")
                    print("2. edit student name")  
                    print("3. edit student address ")
                    print("4. edit contact no. ")
                    studentchoice=int(input("\nwhat you would like to edit : "))
                    if studentchoice==1:
                        update_student_info["id"]=int(input("please enter new student id : ")) 
                        update_student_info["name"]=studentinfo["name"]
                        update_student_info["address"]=studentinfo["address"]
                        update_student_info["contact"]=studentinfo["contact"]
                        studentdata=[]
                        studentdata.append(update_student_info)
                        print("your data is successfully updated")
                        print(studentdata)
                        break       

                    elif studentchoice==2:
                        update_student_info["id"]=studentinfo["id"]
                        update_student_info["name"]=input("please enter new student name : ")
                        update_student_info["address"]=studentinfo["address"]
                        update_student_info["contact"]=studentinfo["contact"]
                        studentdata=[]
                        studentdata.append(update_student_info)
                        print("your data is successfully updated")
                        print(studentdata)
                        break

                    elif studentchoice==3:
                        update_student_info["id"]=studentinfo["id"]
                        update_student_info["name"]=studentinfo["name"]
                        update_student_info["address"]=input("please enter new address : ") 
                        update_student_info["contact"]=studentinfo["contact"]  
                        studentdata=[]
                        studentdata.append(update_student_info)
                        print("your data is successfully updated")
                        print(studentdata)
                        break 

                    elif studentchoice==4:
                        update_student_info["id"]=studentinfo["id"]
                        update_student_info["name"]=studentinfo["name"]
                        update_student_info["address"]=studentinfo["address"]
                        update_student_info["contact"]=int(input("please enter new contact no. : "))
                        studentdata=[]
                        studentdata.append(update_student_info)
                        print("\n your data is successfully updated \n")
                        print(studentdata)
                        break

            elif userinput==3:
                break
            else:
                print("\n invalid input ! \n")

        else:
            print("\n Invalid email and password \n")
    elif menuoption==2:
        print("\n welcome to signup \n")
        studentinfo["id"]=int(input("please enter student id : "))
        studentinfo["name"]=input("please  enter student name : ")
        studentinfo["address"]=input("please enter student address : ")
        studentinfo["contact"]=int(input("please enter student contact no. : "))
        studentdata.append(studentinfo)
        print("\nyou are registered successfully :-)\n")
        menuoption=1
    elif menuoption==3:
        break
    else:
        print("\ninvalid choice \n")


