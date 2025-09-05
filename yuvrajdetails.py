studentdata={}
studentdata["student_id"]=int(input("please enter student id : "))
studentdata["Student_name"]=input("Please enter Student name : ")
studentdata["Fathers_name"]=input("Please enter your Father's name : ")
studentdata["Mothers_name"]=input("Please enter your Mother's name : ")
studentdata["Enrollment_no."]=int(input("Please enter enrollment no : "))
studentdata["Class"]=int(input("Please enter your class : "))
studentdata["Phone_no"]=int(input("Please enter contact number : "))
studentdata["address"]=input("Please enter your address : ")
studentdata["Email"]=input("Please enter email id : ")
studentdata["Age"]=int(input("Please enter your age : "))
studentdata["Height"]=int(input("Please enter student height  : "))
studentdata["Weight"]=int(input("Please enter student weight : "))

del studentdata["name"]
del studentdata["student_id"]


print("------------student details -----------------")
print("student id = ",studentdata["student_id"])
print("Student name = ",studentdata["Student_name"])
print("FAther's name = ",studentdata["Fathers_name"])
print("Mother's name = ",studentdata["Mothers_name"])
print("Enrollment no. = ",studentdata["Enrollment_no."])
print("class = ",studentdata["Class"])
print("contact number = ",studentdata["Phone_no"])
print("Address = ",studentdata["address"])
print("Email = ",studentdata["Email"])
print("Age = ",studentdata["Age"])
print("Height = ",studentdata["Height"])
print(" Weight = ",studentdata["Weight"])
