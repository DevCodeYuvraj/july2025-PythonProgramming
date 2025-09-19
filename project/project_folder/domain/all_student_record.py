def student_record():
    import datetime
    import os
    import json
    
      
    path="filemod-2025/project_folder/database/sample.json"
    with open(path,'r') as file:
        print(file.read())