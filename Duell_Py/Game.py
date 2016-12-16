#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
### Import modules
import os
import sys
from Human import Human
from Computer import Computer
from Tournament import Tournament
from Board import Board
from ViewBoard import ViewBoard
from Die import Die
from random import randrange

class Game(object):
    """Driver for a single instance of a game"""
#* *********************************************************************
#Function Name: __init__
#Purpose: Construct Game Object
#Algorithm:
#1) Create new Human Object
#2) Create new Computer Object
#3) Create new BoardView Object
#4) Create new Board Object
#5) Create new Tournament Object
#Assistance Received: none
#********************************************************************* */
    def __init__(self):
        self.viewBoard = ViewBoard()
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.tournament = Tournament()
    # Getters
    def getHuman(self):
        return self.human
    def getComputer(self):
        return self.computer
    def getBoard(self):
        return self.board
    def getViewBoard(self):
        return self.viewBoard
    def getTournament(self):
        return self.tournament
    # Setters
    def setTournament(self, newTournament):
        self.tournament = newTournament
    def setBoard(self, newBoard):
        self.board = newBoard
    def setHuman(self, newHuman):
        self.human = newHuman
    def setComputer(self, newComputer):
        self.computer = newComputer

    #    /* *********************************************************************
    #Function Name: saveGame
    #Purpose: To save the game to a file
    #Parameters:
    #	nextPlayer, string containing the next player
    #Return Value: void
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	file, ostream object to save the file
    #	fileName, string containing the filename
    #Algorithm:
    #1) Get filename from user
    #2) Loop through gameboard
    #3) Save 0 to file if space is empty
    #4) Write die to file if space is occupied
    #5) Write all the wins and the next player
    #6) Close file
    #Assistance Received: none
    #********************************************************************* */
    def saveGame(self, nextPlayer):
        tempTournament = self.getTournament()
        tempBoardObj = self.getBoard()
        # Get gameboard
        tempBoard = tempBoardObj.getGameBoard()
        print("************************************")
        print("*         ~~ Save Game ~~          *")
        print("************************************")
        print()
        fileName = str(input("Enter File Name: "))
        fileName += ".txt"
        file = open(fileName, "w")
        file.write("Board:\n")
        for row in range(7, -1, -1):
            for col in range(0, 9):
                if(tempBoard[row][col].isEmpty() == True):
                    file.write(" 0  ")
                else:
                    file.write(tempBoard[row][col].displayDie() + " ")
            file.write("\n")
        file.write("\n")
        file.write("Computer Wins: " + str(tempTournament.getComputerWins()) + "\n\n")
        file.write("Human Wins: " + str(tempTournament.getHumanWins()) + "\n\n")
        file.write("Next Player: " + nextPlayer)
        file.close()

    #*********************************************************************
    #Function Name: loadGame
    #Purpose: Load a game from a save file
    #Parameters: None
    #Return Value: void
    #Local Variables:
    #	file, fstream object which contains the loaded file
    #	fileVec, 2D vector of strings which holds all the loaded gameboard in string form
    #	gameBoard, 2D vector of die which holds all the loaded gameboard in die form
    #	nextPlayer, string holding next player from the file
    #	fileName, string containing the file name to open
    #	iss, istringstream to parse out the file
    #Algorithm:
    #1) Get Filename
    #2) Open File
    #3) Loop until end of file
    #4) Using istringstream push each position on the board to the fileVec
    #5) When the board is complete get the number of wins and the next player
    #6) Loop through the fileVec parsing out the die
    #7) Using that data calculate all sides and create a new die
    #8) Push that to the correct position on the gameboard
    #9) Set the board in the game class
    #10) Call startFromLoad
    #Assistance Received: none
    #********************************************************************* */
    def loadGame(self):
        tempBoard = Board()
        tempTournament = Tournament()
        MAX_COL = 9
        MAX_ROW = 8
        rowLine = 0
        strboard = [[]]
        gameboard = [[Die() for j in range(MAX_COL)] for i in range(MAX_ROW)]
        print("************************************")
        print("*         ~~ Load Game ~~          *")
        print("************************************")
        print()
        fileName = str(input("Enter File Name: "))
        fileName += ".txt"
        file = open(fileName, 'r')
        # Skip first line containing Board:
        file.readline()
        for line in file:
            line = line.split(' ')
            for i in line:
                if(i != ''):
                    strboard[rowLine].append(i)
            rowLine += 1
            if(rowLine == MAX_ROW):
                break
            strboard.append([])
        # Skip Blank
        file.readline()
        # Read computer wins string
        computerstr = file.readline()
        computerstr = computerstr.split(' ')
        computerwin = int(computerstr[2])
        # Skip Blank
        file.readline()
        humanstr = file.readline()
        humanstr = humanstr.split(' ')
        humanwin = int(humanstr[2])
        # Skip Blank
        file.readline()
        # Read Next Player
        next = file.readline()
        next = next.split(' ')
        nextPlayer = next[2]

        # Create Board
        iter = 0
        for row in range(7, -1, -1):
            for col in range(0, 9):
                tmp = strboard[row][col]
                if(tmp != "0" and tmp != "0\n"):
                    player = tmp[0]
                    topNum = int(tmp[1])
                    rightNum = int(tmp[2])
                    gameboard[iter][col] = self.board.dieSwitch(topNum, rightNum, player)
            iter += 1

        # Set Objects
        tempBoard.setGameBoard(gameboard)
        tempTournament.setComputerWins(computerwin)
        tempTournament.setHumanWins(humanwin)
        self.setTournament(tempTournament)
        self.setBoard(tempBoard)
        self.startGame(nextPlayer, False)

    #    /* *********************************************************************
    #Function Name: firstPlayer
    #Purpose: To randomly select first player 
    #Parameters:
    #Return Value: The player who will go first
    #Local Variables:
    #human, an int that will contain the random number for the human
    #computer, an int that will contain the random number for the computer
    #player, a string containing the player who will go first
    #Algorithm:
    #1) Seed the random function with the current time
    #2) Start loop which continues if there is a tie
    #3) Randomly select a number 1-6 for human
    #4) Randomly select a number 1-6 for computer
    #5) Compare the two numbers and return the player with highest value
    #Assistance Received: none
    #********************************************************************* */
    def firstPlayer(self):
        while True:
            human = randrange(1, 7)
            computer = randrange(1, 7)
            print("          +=================================================+")
            print("          |        Roll a die to see who goes first!        |")
            print("          |             Please Select an Option             |")
            print("          |                                                 |")
            print("          |        You rolled a " + str(human) + "                           |")
            print("          |        Computer rolled a " + str(computer) + "                      |")
            print("          |                                                 |")
            if(human > computer):
                print("          |        You go first!                            |")
                print("          +=================================================+")
                player = "Human"
                return player
            elif(computer > human):
                print("          |        Computer goes first                      |")
                print("          +=================================================+")
                player = "Computer"
                return player
            elif(computer == human):
                print("          |        It's a tie!                              |")
                print("          |        Roll again...                            |")
                print("          +=================================================+")
                continue

    #    /* *********************************************************************
    #Function Name: displayWinner
    #Purpose: Display the winner of the tournament
    #Parameters: None
    #Return Value: void
    #Local Variables:
    #	computerWins, an int containing the total number of computer wins
    #	humanWins, an int containing the total number of human wins
    #	winner, string containing the winner message
    #Algorithm:
    #1) Check if computerWins > humanWins or vice versa
    #2)	Set appropriate winner string
    #3) Display the total number of wins each and the winner string
    #Assistance Received: none
    #********************************************************************* */
    def displayWinner(self):
        tempTournament = self.getTournament()
        computerWins = tempTournament.getComputerWins()
        humanWins = tempTournament.getHumanWins()
        if (computerWins > humanWins):
            winner = "*                        You lose...                        *";   
        elif (computerWins < humanWins):
            winner = "*                         You win!!!                        *";
        else:
            winner = "*                        It's a tie!                        *";
        print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("*                   ~~ Tournament Results ~~                *")
        print("*     The Computer finished with " + str(computerWins) + " wins                     *")
        print("*     You finished with " + str(humanWins) + " wins                              *")
        print("*                                                           *")
        print(winner)
        print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("~~ Good Bye ~~")
        os.system('pause')
        # Restart the Program
        exit()

    #    /* *********************************************************************
    #Function Name: playAgain
    #Purpose: Ask the player if they would like to play again, if not display winner
    #Parameters: None
    #Return Value: return true to start another game
    #Assistance Received: none
    #********************************************************************* */
    def playAgain(self):
        while True:
            try:
                print("****************************************************")
                print("*     Would you like to play another round?        *")
                print("*     Enter 'y' for yes or 'n' for no              *")
                print("****************************************************")
                print()
                selection = str(input("     Selection: "))
            except ValueError:
                print("Invalid Response. Please try again")
                continue

            if(selection != 'y' and selection != 'n'):
                print("Invalid Response. Please try again")
                continue
            else:
                break
        if(selection == 'y'):
            return True
        elif(selection == 'n'):
            self.displayWinner()
            return False

    #    /* *********************************************************************
    #Function Name: askHel
    #Purpose: Prompt the user if they need help
    #Parameters: None
    #Return Value: Void
    #Assistance Received: none
    #********************************************************************* */
    def askHelp(self):
        tempHuman = self.getHuman()
        while True:
            try:
                print("****************************************************")
                print("*                 ~~ Help? ~~                      *" )
                print("*     Would you like some help?                    *")
                print("*     Enter 'y' for yes or 'n' for no              *")
                print("****************************************************")
                print()
                selection = str(input("     Selection: "))
            except ValueError:
                print("Invalid Response. Please try again")
                continue

            if(selection != 'y' and selection != 'n'):
                print("Invalid Response. Please try again")
                continue
            else:
                break
        if(selection == 'y'):
            tempHuman.help()

    #    /* *********************************************************************
    #Function Name: savePrompt
    #Purpose: Ask user if they would like to save
    #Parameters:
    #	nextPlayer, string containing the next player
    #Return Value: return true if user wishes to save
    #Assistance Received: none
    #********************************************************************* */
    def savePrompt(self, nextPlayer):
        while True:
            try:
                print("****************************************************")
                print("*              ~~ Save & Exit? ~~                  *")
                print("*     Would you like to save and exit the game?    *")
                print("*     Enter 'y' for yes or 'n' for no              *")
                print("****************************************************")
                print()
                selection = str(input("     Selection: "))
            except ValueError:
                print("Invalid Response. Please try again")
                continue

            if(selection != 'y' and selection != 'n'):
                print("Invalid Response. Please try again")
                continue
            else:
                break
        if(selection == 'y'):
            self.saveGame(nextPlayer)
            print()
            print("~~ Good Bye ~~")
            os.system('pause')
            # Exit Program
            exit();
        elif(selection == 'n'):
            return False
    #    /* *********************************************************************
    #Function Name: setWin
    #Purpose: Add a win to the player who has won the game
    #Parameters:
    #	player, string containing the player
    #Return Value: return true on successful execution
    #Algorithm:
    #1) Set win++ depending on the player passed
    #Assistance Received: none
    #********************************************************************* */
    def setWin(self, player):
        tempTournament = self.getTournament()
        tempHuman = self.getHuman()
        tempComputer = self.getComputer()
        if(player == "H"):
            if(tempHuman.checkHumanWin()):
                humanWins = tempTournament.getHumanWins()
                humanWins += 1
                tempTournament.setHumanWins(humanWins)
                self.setTournament(tempTournament)
                return True
        else:
            if(tempComputer.checkComputerWin()):
                computerWins = tempTournament.getComputerWins()
                computerWins += 1
                tempTournament.setComputerWins(computerWins)
                self.setTournament(tempTournament)
                return True
        return False

    #    /* *********************************************************************
    #Function Name: humanMove
    #Purpose: Execute a single round for the human player
    #Return Value: void
    #Algorithm:
    #1) Get the board, human, and viewboard and save to temp objects
    #2) Display the board
    #3) Ask to save
    #4) Set the board in the human class to manipulate
    #5) Ask for help
    #6) Display the board again
    #7) Call the Human play function and set the game class board
    #Assistance Received: none
    #********************************************************************* */
    def humanMove(self):
        tempBoardObj = self.getBoard()
        tempHuman = self.getHuman()
        tempView = self.getViewBoard()
        tempBoard = tempBoardObj.getGameBoard()
        # Display Board
        tempView.displayBoard(tempBoard)
        # Ask Save
        self.savePrompt("Human")
        # Set board in human class
        tempHuman.setBoard(tempBoardObj)
        # Ask Help
        self.askHelp()
        # Display Board again
        tempView.displayBoard(tempBoard)
        # Play and set board
        self.setBoard(tempHuman.play())
        tempHuman.setBoard(self.getBoard())
        self.setHuman(tempHuman)

    #    /* *********************************************************************
    #Function Name: computerMove
    #Purpose: Execute a single round for the computer player
    #Return Value: void
    #Algorithm:
    #1) Get the board, human, and viewboard and save to temp objects
    #2) Display the board
    #3) Ask to save
    #4) Set the board in the computer class to manipulate
    #5) Call the Computer play function and set the game class board
    #Assistance Received: none
    #********************************************************************* */
    def computerMove(self):
        tempBoardObj = self.getBoard()
        tempComputer = self.getComputer()
        tempView = self.getViewBoard()
        tempBoard = tempBoardObj.getGameBoard()
        # Display Board
        tempView.displayBoard(tempBoard)
        # Ask Save
        self.savePrompt("Computer")
        # Set board in Computer class
        tempComputer.setBoard(tempBoardObj)
        # Play and set board
        self.setBoard(tempComputer.play())
        tempComputer.setBoard(self.getBoard())
        self.setComputer(tempComputer)
    #    /* *********************************************************************
    #Function Name: startGame
    #Purpose: Start a round of the game
    #Parameters: None
    #Return Value: void
    #Local Variables:
    #	player, string containing the player who goes first
    #Algorithm:
    #1) Run firstPlayer function to get player who goes first
    #2) Set the boardObj to the game class
    #3) Loop until endGame is true
    #4)		execute a round in the player class
    #5) At end of round, ask player if they would like to play again
    #6) Reset the board
    #7) Recursively run startTournament again
    #Assistance Received: none
    #********************************************************************* */
    def startGame(self, player, newGame):
        tempView = self.getViewBoard()
        if(newGame == True):
            # Get Starting Player
            player = self.firstPlayer()
        endGame = False
        if(player == "Human"):
            while(endGame == False):

                self.humanMove()
                if(self.setWin("H") == True):
                    tempView.displayBoard(self.getBoard().getGameBoard())
                    print()
                    print()
                    print("*****************************************")
                    print("*             You Win!                  *")
                    print("*       Congrats, want a medal?         *")
                    print("*****************************************")
                    print()
                    if(self.playAgain() == True):
                        tempBoard = Board()
                        self.setBoard(tempBoard)
                        self.human.setBoard(tempBoard)
                        self.computer.setBoard(tempBoard)
                        self.startGame("TEMP", True)
                self.computerMove()
                if(self.setWin("C") == True):
                    tempView.displayBoard(self.getBoard().getGameBoard())
                    print()
                    print()
                    print("*****************************************")
                    print("*             You Lose                  *")
                    print("*          Maybe Next Time...           *")
                    print("*****************************************")
                    print()
                    if(self.playAgain() == True):
                        tempBoard = Board()
                        self.setBoard(tempBoard)
                        self.human.setBoard(tempBoard)
                        self.computer.setBoard(tempBoard)
                        self.startGame("TEMP", True)
        else:
            while(endGame == False):
                self.computerMove()
                if(self.setWin("C") == True):
                    tempView.displayBoard(self.getBoard().getGameBoard())
                    print()
                    print()
                    print("*****************************************")
                    print("*             You Lose                  *")
                    print("*          Maybe Next Time...           *")
                    print("*****************************************")
                    print()
                    if(self.playAgain() == True):
                        tempBoard = Board()
                        self.setBoard(tempBoard)
                        self.human.setBoard(tempBoard)
                        self.computer.setBoard(tempBoard)
                        self.startGame()
                self.humanMove()
                if(self.setWin("H") == True):
                    tempView.displayBoard(self.getBoard().getGameBoard())
                    print()
                    print()
                    print("*****************************************")
                    print("*             You Win!                  *")
                    print("*  Next time I won't go so easy on you  *")
                    print("*****************************************")
                    print()
                    if(self.playAgain() == True):
                        tempBoard = Board()
                        self.setBoard(tempBoard)
                        self.human.setBoard(tempBoard)
                        self.computer.setBoard(tempBoard)
                        self.startGame()




