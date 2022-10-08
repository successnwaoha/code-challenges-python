import os
from won import hasWon

os.system("cls")

print("Welcome To ... X & O ...")

gamePlaying = True

values = [
    ["0", "0","0"],
    ["0", "0","0"],
    ["0", "0","0"]
]

def update_values(value, player):
    splitted = value.split(",")
    aCord = int(splitted[0]) - 1
    bCord = int(splitted[1]) - 1
    if values[aCord][bCord] in "XO":
        return False

    values[aCord][bCord] = player
    return True

def vertical_output(values):
    print(values[0])
    print()
    print(values[1])
    print()
    print(values[2])
    print()

player = "X"

while gamePlaying:
    play = input(f"{player} Choose Position eg. a, b: ")
    if play == "end":
        print("Game Over.")
        gamePlaying = False
    while update_values(play, player) == False:
         play = input(f"{player} Choose Position eg. a, b: ")
    
    os.system("cls")
    vertical_output(values)

    won = hasWon(values, play, player)
    if won == True:
        print(f"{player} has won.")
        gamePlaying = False

    if player == "X":
        player = "O"
    else:
        player = "X"