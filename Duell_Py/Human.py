#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
from Player import Player
class Human(Player):
    """Human Class: Executes Human round functions"""
    def __init__(self):
        super().__init__()
        self.startRow = 0
        self.startCol = 0
        self.endRow = 0
        self.endCol = 0
        self.direction = 0
    #    /* *********************************************************************
    #Function Name: setCoordinates
    #Purpose: Set the coordinates mutator
    #Parameters:
    #	startXCoord, startYCood, endXCoord, endYCoord, ints containing the start and end coordinates
    #Return Value: void
    #Assistance Received: none
    #********************************************************************* */
    def setCoordinates(self, startR, startC, endR, endC, directionInput):
        self.startRow = startR
        self.startCol = startC
        self.endRow = endR
        self.endCol = endC
        self.direction = directionInput

    #    /* *********************************************************************
    #Function Name: play
    #Purpose: Execute a round for the Human player
    #Parameters: None
    #Return Value: Pointer to board object
    #Assistance Received: none
    #********************************************************************* */
    def play(self):
        print("It's Your Turn!")
        self.getCoordinates()
        self.getPath(self.startRow, self.startCol, self.endRow, self.endCol, self.direction, False)
        self.getPath(self.startRow, self.startCol, self.endRow, self.endCol, self.direction, True)
        return self.boardObj

    #    /* *********************************************************************
    #Function Name: getCoordinates
    #Purpose: Ask the player for the start and end coordinates and verify selection
    #Parameters: None
    #Return Value: void
    #Local Variables:
    #	x, y, endX, endY, ints containing the start and end coordinates
    #	directionInput, int with the user inputted direction
    #Algorithm:
    #1) Get the coodinates from user
    #2) Get direction from user
    #3) Set all coordinates -1 to match with vector indexes 
    #4) Validate the input to ensure its a legal move
    #5) Set Coordinates
    #Assistance Received: none
    #********************************************************************* */
    def getCoordinates(self):
        tempBoardObj = self.getBoard()
        tempBoard = tempBoardObj.getGameBoard()
        direction = 0
        loop = True
        
        while(loop == True):
            try:
                startRow = int(input("Enter starting row: "))
                startCol = int(input("Enter starting column: "))
                endRow = int(input("Enter destination row: "))
                endCol = int(input("Enter destination column: "))
                print()
            except ValueError:
                print("Invalid Input. Please try again")
                continue

            if(startRow != endRow and startCol != endCol):
                while(True):
                    try:
                        print("Would you like to move Forward or Lateral First?")
                        direction = int(input("Enter '1' for Forward or '2' for Lateral: "))
                    except ValueError:
                        print("Invalid Input. Please try again")
                        continue
                    if(direction != 1 and direction != 2):
                        print("Invalid Input. Please try again")
                        continue
                    else:
                        loop = False
                        break
            else:
                break
        # Set Coordinates minus 1 since board index starts at 0
        startRow -= 1
        startCol -= 1
        endRow -= 1
        endCol -= 1   

        if(self.validateMove(startRow, startCol, endRow, endCol, direction, "H") == True):
            self.setCoordinates(startRow, startCol, endRow, endCol, direction)
            startDie = tempBoard[startRow][startCol].displayDie()
            print("*****************************************************")
            print("*     You are moving " + startDie + " from (" + str(startRow + 1) + "," + str(startCol + 1) + ") to space (" + str(endRow + 1) + "," + str(endCol + 1) + ")  *")
            print("*****************************************************")
        else:
            self.getCoordinates()



