age=int(input("Enter the Age \n"))
if(age<70):
    if(age>18):
        print("Yes you can drive")
    elif(age==18):
        print("Come for physical test")
else:
    print("Sorry you can not drive")