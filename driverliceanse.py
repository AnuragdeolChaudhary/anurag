print("\t\t Welcome to Driving eligible checker\n")
i=1
while i<=1:

    age=int(input("Enter the Age \n"))
    if(age<70):
        if(age>18):
            print(f"Yes you can drive as your age is {age}.")
        elif(age==18):
            print(f"Come for physical test as your age is {age}.")
        else:
            print(f"you cannot drive as your age is {age}.")
        print("\t\tPress 1 to check the age \n \t\tpress 2 to exit")
        i = int(input())
    else:
        print(f"Sorry you can not drive as your age is {age}. ")