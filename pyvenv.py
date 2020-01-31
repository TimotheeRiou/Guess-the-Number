#GUESS THE NUMBER

import random
randomNumber = random.randrange(1,100)                                  #The range goes from 1 to 100
inputUtilisateur = input("enter a number within the range: ")
proposition = int(inputUtilisateur)

while proposition != randomNumber:
    if randomNumber > proposition:
        print("+")
    elif randomNumber < proposition:
        print("-")

    inputUtilisateur = input("enter a number within the range: ")
    proposition = int(inputUtilisateur)

print("OK")
