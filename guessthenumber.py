print("Welcome to the game")
n=10
for i in range(10,0,-1):
    print("Number of Chance left",i)
    x=int(input("Guess the Number = "))
    if(x>n):
        print("Number is greater please choose another number ")
    elif(x==n):
        print("You won the game")
        break
    else:
        print("Number is lesser ")
    print("you loose the game")
