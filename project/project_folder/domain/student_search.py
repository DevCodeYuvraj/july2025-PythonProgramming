def student_search():
    import datetime
    import os
    import json
    flag=0
    path="filemod-2025/project_folder/database/sample.json"
    with open(path,'r') as file:
        data=json.loads(file.read())
        id=input("please enter student qualification id : ")
        for n in data:
            if n["id"]==id:
               
                print(n)
                flag=1
        if flag==0:
            print("student info not found !")        