# if user want 45*3 it will give output as 555
# if user want 56+9 it will give output as 77
# if user want 56/4 it will give output as 4
# and every other opertor will work fine
print("Enter The first Number")
num1=int(input())
print("Enter the Second Number")
num2=int(input())
print("Enter 1 for +\n Enter 2 For - \n Enter 3 For / \n Enter 4 For * \n")
opr=int(input())
if(opr==1):
    print(
        num1,"+",num2,"=",77)
elif(opr==2):
    print(num1,"-",num2,"=",num1-num2)
elif(opr==3):
    print(num1, "/", num2, "=", 4)
elif(opr==4):
    print(num1, "*", num2, "=",555)