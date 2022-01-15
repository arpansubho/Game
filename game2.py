print("\n")
print("\t\t *********Stone,Paper,Scissor Game********* \t\t")
print("Read The Rules Carefully!!:--")
print("There will be 5 rounds of this game and at the end the total score will be counted")
print("1.Type s for stone")
print("2.Type p for paper")
print("3.Type r for scissor")
print("Remember!,Giving input other than the above mentioned would lead to the termination of the game!!")
import random
i=0
while(True):
    w=0
    pc = 0
    uc = 0
    print("\n")
    while i<5:
        i = i + 1
        uchoice = input("Enter your choice:")
        lst = ["s","p","r"]
        pchoice = random.choice(lst)
        if uchoice == pchoice:
            print("matched!")
            continue
        elif uchoice == "s" and pchoice == "p":
            print("Its 0!!")
            pc = pc +1
        elif uchoice == "s" and pchoice == "r":
            print("you won the point!!")
            uc = uc +1
        elif uchoice == "p" and pchoice == "s":
            print("you won the point!!")
            uc = uc +1
        elif uchoice == "p" and pchoice == "r":
            print("Its 0!!")
            pc = pc+1
        elif uchoice == "r" and pchoice == "s":
            print("Its 0!!")
            pc = pc+1
        elif uchoice == "r" and pchoice == "p":
            print("you won the point!!")
            uc = uc +1
        else:
            print("Enter valid input!!")
            w = w +1
            break
    if w==0:
        print("Your Total score",uc)
        print("Total score of computer",pc)
    print("Your message:-")
    if uc>pc and w==0:
        print("\r")
        print("Congrats,You won the game by",uc-pc,"points")
        print("\r")
    elif pc>uc and w==0:
        print("\r")
        print("Sorry!,You lose the game by",pc-uc,"points")
        print("\r")
    elif pc==0 and uc==0 or w!=0:
        print("\r")
        print("Please follow the rules,Game terminated!!")
        print("\r")
    else:
        print("\r")
        print("There was a tie!!,Try again")
        print("\r")
    print("Do you want to play the game again?")
    yc = input("If yes type y:")
    if yc == "y":
        i=0
        continue
    else:
        print("See you next time!!")
        break
