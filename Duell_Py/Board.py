#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
from Die import Die
class Board(object):
    """Board Object manipulates board"""
    #    /* *********************************************************************
    #Function Name: createStartingDie
    #Purpose: Create starting die based off given top number and right number
    #Parameters:
    #	topNum, int containing the top number
    #	rightNum, int containing the right number
    #   player, string containing the player
    #Return Value: die object
    #Algorithm:
    #1) If topNum and rightNum are 1 Create a keypiece
    #2) Else calculate other faces based off given top and right
    #3) return d
    #Assistance Received: none
    #********************************************************************* */
    def createStartingDie(self, topNum, rightNum, playerStr):
        d = Die()
        die = [0] * 6
        keyPiece = False

        # Die[top, bottom, left, right, front, back]
        # When creating a key piece set the keypiece bool to true
        if(topNum == 1 and rightNum == 1):
            die[0] = 1
            die[1] = 1
            die[2] = 1
            die[3] = 1
            die[4] = 1
            die[5] = 1
            keyPiece = True
        else:
            die[0] = topNum
            die[1] = 7 - topNum
            die[2] = 7 - rightNum
            die[3] = rightNum
            die[4] = 4
            die[5] = 3
        d.setDie(die)
        d.setKeyPiece(keyPiece)
        d.setPlayer(playerStr)
        return d

    #    /* *********************************************************************
    #Function Name: Board Constructor __init__
    #Purpose: Construct a Board Object
    #Parameters:
    #Return Value: 
    #Local Variables:
    #gameboard, a 2D list of Die objects
    #Algorithm:
    #1) Inline initialize the 2D list gameboard to the correct size
    #2) Set each of the Dies to the proper starting values and store them in the proper location on the gameboard
    #Assistance Received: none
    #********************************************************************* */
    def __init__(self):
        MAX_COL = 9
        MAX_ROW = 8
        self.gameboard = [[Die() for j in range(MAX_COL)] for i in range(MAX_ROW)]
        # Computer Starting Positions
        self.gameboard[7][0] = self.createStartingDie(5, 6, "C")
        self.gameboard[7][1] = self.createStartingDie(1, 5, "C")
        self.gameboard[7][2] = self.createStartingDie(2, 1, "C")
        self.gameboard[7][3] = self.createStartingDie(6, 2, "C")
        self.gameboard[7][4] = self.createStartingDie(1, 1, "C")
        self.gameboard[7][5] = self.createStartingDie(6, 2, "C")
        self.gameboard[7][6] = self.createStartingDie(2, 1, "C")
        self.gameboard[7][7] = self.createStartingDie(1, 5, "C")
        self.gameboard[7][8] = self.createStartingDie(5, 6, "C")

        # Human Starting Positions
        self.gameboard[0][0] = self.createStartingDie(5, 6, "H")
        self.gameboard[0][1] = self.createStartingDie(1, 5, "H")
        self.gameboard[0][2] = self.createStartingDie(2, 1, "H")
        self.gameboard[0][3] = self.createStartingDie(6, 2, "H")
        self.gameboard[0][4] = self.createStartingDie(1, 1, "H")
        self.gameboard[0][5] = self.createStartingDie(6, 2, "H")
        self.gameboard[0][6] = self.createStartingDie(2, 1, "H")
        self.gameboard[0][7] = self.createStartingDie(1, 5, "H")
        self.gameboard[0][8] = self.createStartingDie(5, 6, "H")

    # Getter
    def getGameBoard(self):
        return self.gameboard
    # Setter
    def setGameBoard(self, board):
        self.gameboard = board

    #    /* *********************************************************************
    #Function Name: createDie
    #Purpose: Create die based off sides
    #Parameters:
    #	topNum, int containing the top number
    #	rightNum, int containing the right number
    #	frontNum, int containing front number
    #	backNum, int containing back number
    #	player, string containing the player
    #Return Value: die object
    #Algorithm:
    #1) If topNum and rightNum are 1 Create a keypiece
    #2) Else calculate other faces based off given sides
    #3) return d
    #Assistance Received: none
    #********************************************************************* */
    def createDie(self, topNum, rightNum, frontNum, backNum, player):
        d = Die()
        die = [0] * 6
        keyPiece = False

        # Die[top, bottom, left, right, front, back]
        # When creating a key piece set the keypiece bool to true
        if(topNum == 1 and rightNum == 1):
            die[0] = 1
            die[1] = 1
            die[2] = 1
            die[3] = 1
            die[4] = 1
            die[5] = 1
            keyPiece = True
        else:
            die[0] = topNum
            die[1] = 7 - topNum
            die[2] = 7 - rightNum
            die[3] = rightNum
            die[4] = frontNum
            die[5] = backNum
        d.setDie(die)
        d.setKeyPiece(keyPiece)
        d.setPlayer(player)
        return d

    #    /* *********************************************************************
    #Function Name: dieSwitch
    #Purpose: To create the Die pieces on load game
    #Parameters:
    #topNum, an int containing the top number
    #rightNum, an int containing the right number
    #player, a string containing the player
    #Return Value: A Die pointer to the newly created Die
    #Local Variables:
    #d, a pointer to a new Die()
    #Algorithm:
    #1) Create a new die, d
    #2) Enter switch statement with value of top number
    #3) Execute nested switch statement with value of the right number
    #4) Create a Die with the given top, right, and front back from switch statement
    #and set to d
    #5) break out of switches
    #6) Return d
    #Assistance Received: none
    #********************************************************************* */
    def dieSwitch(self, topNum, rightNum, player):
        # Die[top, bottom, left, right, front, back]
        d = Die()
        if(topNum == 1):
            if(rightNum == 1):
                d = self.createDie(topNum, rightNum, 1, 1, player)
            elif(rightNum == 2):
                d = self.createDie(topNum, rightNum, 3, 4, player)
            elif(rightNum == 3):
                d = self.createDie(topNum, rightNum, 5, 2, player)
            elif(rightNum == 4):
                d = self.createDie(topNum, rightNum, 2, 5, player)
            elif(rightNum == 5):
                d = self.createDie(topNum, rightNum, 4, 3, player)
        elif(topNum == 2):
            if(rightNum == 1):
                d = self.createDie(topNum, rightNum, 4, 3, player)
            elif(rightNum == 3):
                d = self.createDie(topNum, rightNum, 1, 6, player)
            elif(rightNum == 4):
                d = self.createDie(topNum, rightNum, 6, 1, player)
            elif(rightNum == 6):
                d = self.createDie(topNum, rightNum, 3, 4, player)
        elif(topNum == 3):
            if(rightNum == 1):
                d = self.createDie(topNum, rightNum, 2, 5, player)
            elif(rightNum == 2):
                d = self.createDie(topNum, rightNum, 6, 1, player)
            elif(rightNum == 5):
                d = self.createDie(topNum, rightNum, 1, 6, player)
            elif(rightNum == 6):
                d = self.createDie(topNum, rightNum, 5, 2, player)
        elif(topNum == 4):
            if(rightNum == 1):
                d = self.createDie(topNum, rightNum, 5, 2, player)
            elif(rightNum == 2):
                d = self.createDie(topNum, rightNum, 1, 6, player)
            elif(rightNum == 5):
                d = self.createDie(topNum, rightNum, 6, 1, player)
            elif(rightNum == 6):
                d = self.createDie(topNum, rightNum, 2, 5, player)
        elif(topNum == 5):
            if(rightNum == 1):
                d = self.createDie(topNum, rightNum, 3, 4, player)
            elif(rightNum == 3):
                d = self.createDie(topNum, rightNum, 6, 1, player)
            elif(rightNum == 4):
                d = self.createDie(topNum, rightNum, 1, 6, player)
            elif(rightNum == 6):
                d = self.createDie(topNum, rightNum, 4, 3, player)
        elif(topNum == 6):
            if(rightNum == 2):
                d = self.createDie(topNum, rightNum, 4, 3, player)
            elif(rightNum == 3):
                d = self.createDie(topNum, rightNum, 2, 5, player)
            elif(rightNum == 4):
                d = self.createDie(topNum, rightNum, 5, 2, player)
            elif(rightNum == 5):
                d = self.createDie(topNum, rightNum, 3, 4, player)
        return d

    #########################################
    #           Die Moving Functions        #
    #########################################
    #    /* *********************************************************************
    #Function Name: movePieceUp
    #Purpose: Move the Die from gameboard[y][x] --> gameboard[y+1][x]
    #Parameters:
    #row, col, ints containing the x and y coordinates
    #Return Value: void
    #Local Variables:
    #player, string that gets player based off gameboard[y][x]
    #newDie, pointer to a new Die object used to replace the previous piece
    #Algorithm:
    #1) Get player from gameboard[y][x].getPlayer();
    #2) The player determines if the Die is going to roll forward or backward when moving Up
    #3) If it's a human die, roll Die forward one roll, move Up one space, replace old space with a new empty die
    #4) If it's a computer die, roll Die backward one roll, move Up one space, replace old space with a new empty die
    #5) set the gameboard to the Board class
    #Assistance Received: none
    #********************************************************************* */
    def movePieceUp(self, row, col):
        tempBoard = self.getGameBoard()
        player = tempBoard[row][col].getPlayer();
        emptyDie = Die()
        if(player == 'H'):
            tempBoard[row][col].frontalMove()
        else:
            tempBoard[row][col].backwardMove()
        tempBoard[row + 1][col] = tempBoard[row][col]
        tempBoard[row][col] = emptyDie
        self.setGameBoard(tempBoard)

    #/* *********************************************************************
    #Function Name: movePieceDown
    #Purpose: Move the Die from gameboard[y][x] --> gameboard[y-1][x]
    #Parameters:
    #row, col, ints containing the x and y coordinates
    #Return Value: void
    #Local Variables:
    #player, string that gets player based off gameboard[y][x]
    #newDie, pointer to a new Die object used to replace the previous piece
    #Algorithm:
    #1) Get player from gameboard[y][x].getPlayer();
    #2) The player determines if the Die is going to roll foward or backward when moving down
    #3) If it's a human die, roll Die backward one roll, move down one space, replace old space with a new empty die
    #4) If it's a computer die, roll Die forward one roll, move down one space, replace old space with a new empty die
    #5) set the gameboard to the Board class
    #Assistance Received: none
    #********************************************************************* */
    def movePieceDown(self, row, col):
        tempBoard = self.getGameBoard()
        player = tempBoard[row][col].getPlayer();
        emptyDie = Die()
        if(player == 'H'):
            tempBoard[row][col].backwardMove()
        else:
            tempBoard[row][col].frontalMove()
        tempBoard[row - 1][col] = tempBoard[row][col]
        tempBoard[row][col] = emptyDie
        self.setGameBoard(tempBoard)

    #/* *********************************************************************
    #Function Name: movePieceLeft
    #Purpose: Move the Die from gameboard[y][x] --> gameboard[y][x-1]
    #Parameters:
    #x, y, ints containing the x and y coordinates
    #Return Value: void
    #Local Variables:
    #player, string that gets player based off gameboard[y][x]
    #newDie, pointer to a new Die object used to replace the previous piece
    #Algorithm:
    #1) Get player from gameboard[y][x].getPlayer();
    #2) The player determines if the Die is going to roll left or right when moving right
    #3) If it's a human die, roll Die left one roll, move left one space, replace old space with a new empty die
    #4) If it's a computer die, roll Die right one roll, move right one space, replace old space with a new empty die
    #5) set the gameboard to the Board class
    #Assistance Received: none
    #********************************************************************* */
    def movePieceLeft(self, row, col):
        tempBoard = self.getGameBoard()
        player = tempBoard[row][col].getPlayer();
        emptyDie = Die()
        if(player == 'H'):
            tempBoard[row][col].lateralLeftMove()
        else:
            tempBoard[row][col].lateralRightMove()
        tempBoard[row][col - 1] = tempBoard[row][col]
        tempBoard[row][col] = emptyDie
        self.setGameBoard(tempBoard)

    #    /* *********************************************************************
    #Function Name: movePieceRight
    #Purpose: Move the Die from gameboard[y][x] --> gameboard[y][x+1]
    #Parameters:
    #x, y, ints containing the x and y coordinates
    #Return Value: void
    #Local Variables:
    #player, string that gets player based off gameboard[y][x]
    #newDie, pointer to a new Die object used to replace the previous piece
    #Algorithm:
    #1) Get player from gameboard[y][x].getPlayer();
    #2) The player determines if the Die is going to roll left or right when moving right
    #3) If it's a human die, roll Die right one roll, move right one space, replace old space with a new empty die
    #4) If it's a computer die, roll Die left one roll, move right one space, replace old space with a new empty die
    #5) set the gameboard to the Board class
    #Assistance Received: none
    #********************************************************************* */
    def movePieceRight(self, row, col):
        tempBoard = self.getGameBoard()
        player = tempBoard[row][col].getPlayer();
        emptyDie = Die()
        if(player == 'H'):
            tempBoard[row][col].lateralRightMove()
        else:
            tempBoard[row][col].lateralLeftMove()
        tempBoard[row][col + 1] = tempBoard[row][col]
        tempBoard[row][col] = emptyDie
        self.setGameBoard(tempBoard)