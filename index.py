import random

print("you have to print within 0-3")
def function1():
    list=[1,2,3]
    comp=random.choice(list)
    user=int(input("enter your number: "))
    print("comp enter: ",comp)
    if user==1:
        print("snake")
    elif user==2:
        print("water")
    elif user==3:
        print("gun")
    if comp==1:
        print("snake")
    elif comp==2:
        print("water")
    elif comp==3:
        print("gun")
    if user==comp:
        print("game draw")
    elif user==1 and comp==2:
        print("you win")
    elif user==2 and comp==1:
        print("you lose")
    elif user==2 and comp==3:
        print("you win")
    elif user==3 and comp==2:
        print("you lose")
    elif user==1 and comp==3:
        print("you lose")
    elif user==3 and comp==1:
        print("you win")
    print("Do You wat to play if Yes press 1 if no press 0")
    user1=int(input("enter your press: "))
    if user1==0:
        print("You ended game")
        return 0
    else:
        function1()

function1()
