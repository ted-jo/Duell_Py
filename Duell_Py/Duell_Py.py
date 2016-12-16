#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
### Import modules
from Game import Game

print(" +********************************************************************************************************+ ")
print(" |  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.    |")
print(" |  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  |")
print(" |  | |  ________    | || | _____  _____ | || |  _________   | || |   _____      | || |   _____      | |  |")
print(" |  | | |_   ___ `.  | || ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |  |_   _|     | |  |")
print(" |  | |   | |   `. \\ | || |  | |    | |  | || |   | |_  \\_|  | || |    | |       | || |    | |       | |  |")
print(" |  | |   | |    | | | || |  | '    ' |  | || |   |  _|  _   | || |    | |   _   | || |    | |   _   | |  |")
print(" |  | |  _| |___.' / | || |   \\ `--' /   | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |__/ |  | |  |")
print(" |  | | |________.'  | || |    `.__.'    | || | |_________|  | || |  |________|  | || |  |________|  | |  |")
print(" |  | |              | || |              | || |              | || |              | || |              | |  |")
print(" |  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  |")
print(" |  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'    |")
print(" |                                                                                                        |")
print(" |       Author: Ted Johansmeyer                                                                          |")
print(" |       Project: Duell Python                                                                            |")
print(" |       Class: CMPS 366 Organization of Programming Languages                                            |")
print(" |       Date: December 13th 2016                                                                         |")
print(" |                                                                                                        |")
print(" +********************************************************************************************************+")
print()
while True:
    try:
        print("          +=================================================+")
        print("          |                Welcome to Duell!                |")
        print("          |             Please Select an Option             |")
        print("          |                                                 |")
        print("          |     1. Start a New Tournament                   |")
        print("          |     2. Load a Saved Game                        |")
        print("          |     3. Quit                                     |")
        print("          +=================================================+")
        print()
        selection = int(input("Selection: "))
    except ValueError:
        print("Invalid Response. Please try again")
        continue

    if(selection != 1 and selection != 2 and selection != 3):
        print("Invalid Response. Please try again")
        continue
    else:
        break
if (selection == 1):
    # Start a New Game 
    game = Game()
    game.startGame("TEMP", True)
elif(selection == 2):
    game = Game()
    game.loadGame()
else:
    # Quit
    exit()