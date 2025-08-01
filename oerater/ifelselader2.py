#check pass and fail
marks1=int(input("Enter mark 1: "))
marks2=int(input("Enter mark 2: "))
marks3=int(input("Enter mark 2: "))

total_percentage = (marks1 + marks2 + marks3) / 300
if(total_percentage<=40):
    print("pass")
elif(total_percentage<=33):
    print("compartment")
else:
    print("fail")