studentinfo=[]
studentdata={}
qualificationdictinfo={}
qualificationlist=[]
numberofstudents=int(input("please enter no of students you want to register (1-3): "))

if numberofstudents==1:

    studentdata["id"]=int(input("please enter 1st student id : "))
    studentdata["name"]=input("please enter 1st student name : ") 
    studentdata["address"]=input("please enter 1st student address : ")
    numberofqualification=int(input("please enter no qualification your want to submit (1-3) : "))

    if numberofqualification==1:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==2:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==3:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 3rd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    else:
        print("invalid input ! please enter number between (1-3)")    

    studentinfo.append(studentdata)
elif numberofstudents==2:

    studentdata["id"]=int(input("please enter 1st student id : "))
    studentdata["name"]=input("please enter 1st student name : ") 
    studentdata["address"]=input("please enter 1st student address : ")
    numberofqualification=int(input("please enter no qualification your want to submit (1-3) : "))

    if numberofqualification==1:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==2:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==3:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 3rd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    else:
        print("invalid input ! please enter number between (1-3)")    

    studentinfo.append(studentdata)
    
    studentdata={}

    studentdata["id"]=int(input("please enter 2nd student id : "))
    studentdata["name"]=input("please enter 2nd student name : ") 
    studentdata["address"]=input("please enter 2nd student address : ")
    numberofqualification=int(input("please enter no qualification your want to submit (1-3) : "))

    if numberofqualification==1:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==2:
        qualificationdictinfo["name"]=input("please enter 1stqualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==3:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 3rd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    else:
        print("invalid input ! please enter number between (1-3)")    
        
        studentinfo.append(studentdata)

elif numberofstudents==3:
    studentdata["id"]=int(input("please enter 1st student id : "))
    studentdata["name"]=input("please enter 1st student name : ") 
    studentdata["address"]=input("please enter 1st student address : ")
    numberofqualification=int(input("please enter no qualification your want to submit (1-3) : "))

    if numberofqualification==1:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==2:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==3:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2ndqualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 3rd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    else:
        print("invalid input ! please enter number between (1-3)")    

    studentinfo.append(studentdata)
    
    studentdata={}
    studentdata["id"]=int(input("please enter 2nd student id : "))
    studentdata["name"]=input("please enter 2nd student name : ") 
    studentdata["address"]=input("please enter 2nd student address : ")
    numberofqualification=int(input("please enter no qualification your want to submit (1-3) : "))

    if numberofqualification==1:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==2:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==3:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 3rd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    else:
        print("invalid input ! please enter number between (1-3)")    

    studentinfo.append(studentdata)
    
    studentdata={}


    studentdata["id"]=int(input("please enter 3rd student id : "))
    studentdata["name"]=input("please enter 3rd student name : ") 
    studentdata["address"]=input("please enter 3rd student address : ")
    numberofqualification=int(input("please enter no qualification your want to submit (1-3) : "))

    if numberofqualification==1:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==2:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    elif numberofqualification==3:
        qualificationdictinfo["name"]=input("please enter 1st qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 2nd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        qualificationdictinfo={}
        qualificationdictinfo["name"]=input("please enter 3rd qualification : ")
        qualificationdictinfo["passingyear"]=int(input("please enter your passing year : "))
        qualificationlist.append(qualificationdictinfo)
        studentdata["qualification"]=qualificationlist
    else:
        print("invalid input ! please enter number between (1-3)")    
        
        studentinfo.append(studentdata)
else:
    print("invalid value! please enter value between (1-3)")


print(studentinfo[1])