import random


choice = input("rock paper or scissors: ")
cnum = random.randint(1,3)
if choice == "rock":
    pnum = 1
elif choice == "paper":
    pnum = 2
elif choice == "scissors":
    pnum = 3


if pnum == cnum:
    print("you tied with computer")
elif pnum == 1 and cnum == 2:
    print("Computer won")
elif pnum == 2 and cnum == 1:
    print("You won")
elif pnum == 3 and cnum == 2:
    print("you won")
elif pnum == 3 and cnum == 1:
    print("computer won")
elif pnum == 2 and cnum == 3:
    print("computer won")
elif pnum == 1 and cnum == 3:
    print("you won")
