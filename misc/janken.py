import random

def poi():
    choice=["Rock", "Paper", "Scissors"]
    opponent=choice[random.randint(0, 2)]
    player=False

    while player==False:
        player=input("Rock, Paper, Scissors?")
        if player==opponent:
            print("Tie!")
        elif player=="Rock":
            if opponent=="Paper":
                print("You lose!", opponent, "covers", player)
            else:
                print("You win!", player, "smashes", opponent)
        elif player=="Paper":
            if opponent=="Scissors":
                print("You lose!", opponent, "cut", player)
            else:
                print("You win!", player, "covers", opponent)
        elif player=="Scissors":
            if opponent=="Rock":
                print("You lose...", opponent, "smashes", player)
            else:
                print("You win!", player, "cut", opponent)
        else:
            print("That's not a valid play. Check your spelling!")

        opponent=choice[random.randint(0, 2)]
        player=False
