import random
import time
l=time.asctime(time.localtime(time.time()))
print(l)
uwin=0
swin=0
mylist=["s","w","g"]
print("\n\t\t\tWelcome to the the Snake Game\n")
for j in range(10,0,-1):
    system = random.choice(mylist)
    y=input("Enter S for snake\n Enter W for Water\n Enter G for gun \n==  ")
    user=y.lower()
    if user==system:
        print("Tie")
        print(f"System Choose {system}")
        time.sleep(2)
    elif user=="s" and system=="w":
        print("user Win")
        print(f"System Choose {system}")
        uwin=uwin+1
        print(f"User points = {uwin} ")
        time.sleep(2)
    elif user=="w" and system =="s":
        print("Computer Wins")
        print(f"System Choose {system}")
        swin = swin + 1
        print(f"Computer points = {swin}")
        time.sleep(2)
    elif user=="s" and system=="g":
        print("Computer Wins")
        print(f"System Choose = {system}")
        swin = swin + 1
        print(f"Computer points = {swin} ")
        time.sleep(2)
    elif user=="g" and system=="s":
        print("User Wins")
        print(f"System Choose = {system}")
        uwin = uwin + 1
        print(f"User points = {uwin} ")
        time.sleep(2)
    else:
        print("No One win!")
if(swin>uwin):
    print(f"Computer Win By {swin-uwin} Points")
else:
    print(f"User Win By {uwin-swin} points")
    time.sleep(10)