import random
i=0
while i<2:
    print("Enter 1 for password generate 2 for exit")
    i=int(input())
    l=["a","b","c","d","e","f""g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    u=["A","B","C","D","E","F""G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    s=["!","@","#","$","%","&"]
    r1=random.choice(l)
    r2=random.choice(u)
    r3=random.choice(s)
    r4=random.choice(u)
    r5=random.choice(l)
    r6=random.choice(s)
    password=r1+r2+r3+r4+r5+r6
    print(f"password is = {password}")