import project_folder
while(True):
    choice=project_folder.menu()
    if choice=='1':
        project_folder.student_registration()
    elif choice=='2':
        project_folder.student_search()    
    elif choice=='3':
        project_folder.student_record()
    elif choice=='4':
        break
    else:
        print("enter correct value")