import random
import time
k=0
while k<3:
    print("\nEnter 1 to generate Password \n Enter 2 to generate Password \nEnter 3 to quit Password \n==")
    k=int(input())
    if k==1:
        y=random.randrange(1000,9999)
        print(f"Your Otp is {y}")
        time.sleep(2)
    elif k==2:
        l = ["a", "b", "c", "d", "e", "f""g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
             "w", "x", "y", "z"]
        u = ["A", "B", "C", "D", "E", "F""G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
             "W", "X", "Y", "Z"]
        s = ["!", "@", "#", "$", "%", "&"]
        r1 = random.choice(l)
        r2 = random.choice(u)
        r3 = random.choice(s)
        r4 = random.choice(u)
        r5 = random.choice(l)
        r6 = random.choice(s)

        password = r1 + r2 + r3 + r4 + r5 + r6
        print(f"Password is = {password}")
        time.sleep(2)
    elif k==3:
        print("Quit Successfully")
    else:
        print("wrong Input please reset the program")