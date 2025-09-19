import datetime
import os
import json


path="filemod-2025/project_folder/database/sample.json"

schooldata=[]

def Readfile_fromjson():
    with open(path,'r') as file:
            data=json.loads(file.read()) 
            return data


def student_registration():
        
        schooldata=Readfile_fromjson()
        qualification=[]
        studentdata={}
        id=input("Please enter student id : ")
        name=input("please enter student name :")
        email=input("please enter student email :")
        address=input("please enter your address : ")
        
        studentdata["id"]=id
        studentdata["name"]=name
        studentdata["email"]=email
        studentdata["address"]=address
        studentdata["registration_date"]=str(datetime.datetime.now())
        while(True):
            userchoice=input("do you want to add qualifications (yes/no) :")
            if userchoice=='yes':
                qual={}
                qual["qualification_name"]=input("enter your qualification name :")
                qual["qualification_year"]=input("enter your qualifiacation year : ")
                qualification.append(qual)
                studentdata["qualification"]=qualification
            elif userchoice=='no':
                break       
        

        schooldata.append(studentdata)
        with open(path,'w') as file:
            jsonoutput=json.dumps(schooldata,indent=2)
            file.write(jsonoutput)
        
        
            