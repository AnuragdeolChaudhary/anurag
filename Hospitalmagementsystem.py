import time
import os

print("\t\t\t\t\tWelcome To Hospital Management")

x=0
while x<4:
    l = time.asctime(time.localtime(time.time()))
    print("Enter 1 for Patient Register \n Enter 2 To get Details Of Patients\n Enter 3 for exit the data ")
    x=int(input())
    if x==1:
        print("Please enter Patient ID")
        y=input()

        if os.path.isfile(y + ".txt"):
            print("File exist please use another id")
        else:
            f = open(y + ".txt", "a+")
            f.write(f"{l}   \n Your ID is \t")
            f.write(y)
            print("Enter Your Full Name")
            nam=input()
            f.write(f"\n Name {nam}")
            print("Enter Mobile Number")
            f.write("\n")
            f.write("Mobile \t")
            f.write(input())
            print("Enter Room Number")
            f.write("\n")
            f.write("Room Number \t")
            f.write(input())
            f.write("\n")
            print("Enter father name")
            f.write("Father Name : \t")
            f.write(input())
            f.close()
            print(f"Please ID is {y}")
            print("Data Successfully uploaded")
    elif x==2:
         try:
             print("Please Enter  Id")
             y=input()
             f = open(y + ".txt", "r")
             c=f.read()
             print(c)
             f.close()
             time.sleep(15)
         except Exception as e:
             print(e)
             print("This patient is not present")

print("exit Successfully")