print("Welcome to indixpert ! ")
data=[]
info={}
count=0
flag=0
login={}
while(True):
    print("1. for signup")
    print("2. for login" )
    print("3. for exit")
    choice=input("please enter your choice : ")
    choice=choice.strip()
    while(True):

        if choice.isdigit():
            if choice=='1':
                info={}
                info["user_name"]=input("please enter your username : ")
                info["user_name"]=info["user_name"].strip()
                if info["user_name"].isalpha():
                    info["password"]=input("please create your password :")
                    length=info["password"].__len__()
                    if length>=8:
                        info["password1"]=input("please condirm your password : ")
                        if info["password"]==info["password1"]:
                            info["email"]=input("please enter your email id")
                            if info["email"].count("@gmail.com")>=1:
                                info["address"]=input("please enter your address : ")
                                data.append(info)
                                
                                count+=1
                                if count==2:
                                    break

                            else:
                                print("please enter valid email :")    
                        else:
                            print("password not matched , please try again :")
                            
                    else:
                        print("enter more than 8 characher")
                else:
                    print("please use only characters :")
        elif choice==2:
            login["user_name"]=input("please enter username_id: ")
            login["password"]=input("please enter password: ")
            for n in data:
                if n["user_name"]==login["user_name"] and n["password"]==login["password"]:
                    flag=1
                    if flag==1:
                        print("logged in successfully")
                        break
        elif choice==3:
            break
        else:
            print("enter valid choice")


