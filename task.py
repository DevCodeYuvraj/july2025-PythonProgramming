positive=0
negative=0

num1=int(input("please enter any number : "))
num2=int(input("please enter any number : "))
num3=int(input("please enter any number : "))
num4=int(input("please enter any number : "))
num5=int(input("please enter any number : "))

if num1>=0:
    positive+=1
else:
    negative+=1

if num2>=0:
    positive+=1
else:
    negative+=1

if num3>=0:
    positive+=1
else:
    negative+=1
    
if num4>=0:
    positive+=1
else:
    negative+=1
if num5>=0:

    positive+=1
else:
    negative+=1
    
print(" positive numbers = ",positive)

print(" negative numbers =",negative)
