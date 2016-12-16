#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
from Board import Board

class Player(object):
    """Player Object, Contains AI functions and path checking"""
    def __init__(self):
        self.boardObj = Board()
    # Getter 
    def getBoard(self):
        return self.boardObj
    # Setter
    def setBoard(self, board):
        self.boardObj = board
    #    /* *********************************************************************
    #Function Name: checkOOB
    #Purpose: Function checks to make sure coordinates are not out of bounds
    #Parameters:
    #	row & col, ints containing the coordinates of the piece to move
    #Return Value: return true if move is in bounds
    #Local Variables: None
    #Assistance Received: none
    #********************************************************************* */
    def checkOOB(self, row, col):
    	# Check if x or y coordinate is out of the 2D vector bounds on the upper end
        if (col > 8 or row > 7):
            return False
	    # Check if x or y is out of the 2D vector bounds on the low end
        elif (col < 0 or row < 0):
            return False
        return True

    #    /* *********************************************************************
    #Function Name: checkVerticalPath
    #Purpose: This function either checks or executes the move in the vertical direction
    #Parameters:
    #startX, startY, endX, endY, ints containing the start and end coordinates
    #execute, a bool that determines if the function will actually move the die
    #Return Value: returns true if the check or move is complete
    #Local Variables:
    #tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #player, string containing the player at the start location
    #oppositePlayer, a bool signifying if an opponents die is at the end location
    #first, a bool that flips after the first loop iteration to skip it
    #tempY, an int set to 1 +- endY so the check stops before the end space
    #Algorithm:
    #1) If startY > endY, check the downward movement of the starting piece
    #2)		set tempY to 1 above the endX
    #3)		Loop starting from StartY as long as startY > endY
    #4)			If execute is false, check board at every StartY in loop to see if space is empty
    #5)				If the end space is an opposing die on return true so it can overtake
    #6)			If execute is true, call the movePieceDown function every iteration of the loop
    #7)		return true on successful completion
    #8) If startY < endY do opposite and call movePieceUp to move the die up on the board
    #Assistance Received: none
    #********************************************************************* */
    def checkVerticalPath(self, startRow, startCol, endRow, endCol, execute):
        tempBoard = self.boardObj.getGameBoard()
        first = True
        if(startRow > endRow):
            while(startRow >= endRow):
                # If execute is false only check path
                if(execute == False):
                    if(first == True):
                        # Skip starting space
                        first = False
                        startRow -= 1
                        continue
                    # If the end space is on an opposing die return true
                    if(startCol == endCol and startRow == endRow and tempBoard[startRow][startCol].isEmpty() == False):
                        return True
                    # Return false if path is blocked
                    if(tempBoard[startRow][startCol].isEmpty() == False):
                        return False
                else:
                    if(startRow == endRow):
                        return True
                    else:
                        # If execute is true execute the move
                        self.boardObj.movePieceDown(startRow, startCol)
                startRow -= 1
            return True
        elif(startRow < endRow):
            while(startRow <= endRow):
                if(execute == False):
                    if(first == True):
                        first = False
                        startRow += 1
                        continue
                    if(startCol == endCol and startRow == endRow and tempBoard[startRow][startCol].isEmpty() == False):
                        return True
                    if(tempBoard[startRow][startCol].isEmpty() == False):
                        return False
                else:
                    if(startRow == endRow):
                        return True
                    else:
                        self.boardObj.movePieceUp(startRow, startCol)
                startRow += 1
            return True

    #    /* *********************************************************************
    #Function Name: checkHorizontalPath
    #Purpose: This function either checks or executes the move in the horizontal direction
    #Parameters:
    #startX, startY, endX, endY, ints containing the start and end coordinates
    #execute, a bool that determines if the function will actually move the die
    #Return Value: returns true if the check or move is complete
    #Local Variables:
    #tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #player, string containing the player at the start location
    #oppositePlayer, a bool signifying if an opponents die is at the end location
    #first, a bool that flips after the first loop iteration to skip it
    #tempX, an int set to 1 +- endX so the check stops before the end space
    #Algorithm:
    #1) If startX > endX, check the lateral left movement of the starting piece
    #2)		set tempX to 1 above the endX
    #3)		Loop starting from StartY as long as startY > endY
    #4)			If execute is false, check board at every StartX in loop to see if space is empty
    #5)				If the end space is an opposing die on return true so it can overtake
    #6)			If execute is true, call the movePieceLeft function every iteration of the loop
    #7)		return true on successful completion
    #8) If startX < endX do opposite and call movePieceRight to move the die right on the board
    #Assistance Received: none
    #********************************************************************* */
    def checkHorizontalPath(self, startRow, startCol, endRow, endCol, execute):
        tempBoard = self.boardObj.getGameBoard()
        first = True
        if(startCol > endCol):
            while(startCol >= endCol):
                # If execute is false only check path
                if(execute == False):
                    if(first == True):
                        # Skip starting space
                        first = False
                        startCol -= 1
                        continue
                    # If the end space is on an opposing die return true
                    if(startCol == endCol and startRow == endRow and tempBoard[startRow][startCol].isEmpty() == False):
                        return True
                    # Return false if path is blocked
                    if(tempBoard[startRow][startCol].isEmpty() == False):
                        return False
                else:
                    if(startCol == endCol):
                        return True
                    else:
                        # If execute is true execute the move
                        self.boardObj.movePieceLeft(startRow, startCol)
                startCol -= 1
            return True
        elif(startCol < endCol):
            while(startCol <= endCol):
                if(execute == False):
                    if(first == True):
                        first = False
                        startCol += 1
                        continue
                    if(startCol == endCol and startRow == endRow and tempBoard[startRow][startCol].isEmpty() == False):
                        return True
                    if(tempBoard[startRow][startCol].isEmpty() == False):
                        return False
                else:
                    if(startCol == endCol):
                        return True
                    else:
                        self.boardObj.movePieceRight(startRow, startCol)
                startCol += 1
            return True

    #/* *********************************************************************
    #Function Name: getDirection()
    #Purpose: This function finds direction to move with a clear path
    #Parameters:
    #	startX, startY, endX, endY, ints containing the start and end coordinates
    #Return Value: an int which signifies the direction chosen
    #Local Variables: None
    #Algorithm:
    #1) If startX = endX, return 0 if the vertical path is clear
    #2) If startY = endY, return 0 if the horizontal path is clear
    #3) If the vertical path then the horizontal path is clear, return 1
    #4) If the horizontal path then the vertical path is clear, return 2
    #5) If no path is clear return -1
    #Assistance Received: none
    #********************************************************************* */
    def getDirection(self, startRow, startCol, endRow, endCol):
        # Return 0 if strictly vertical or strictly horizontal move
        if (startCol == endCol):
            if (self.checkVerticalPath(startRow, startCol, endRow, endCol, False) == True):
                return 0
        elif(startRow == endRow):
            if (self.checkHorizontalPath(startRow, startCol, endRow, endCol, False) == True):
                return 0
        elif (self.checkVerticalPath(startRow, startCol, endRow, endCol, False) == True):
            # Check forward then horizontal path and return 1
            if (self.checkHorizontalPath(endRow, startCol, endRow, endCol, False) == True):
                return 1
        elif (self.checkHorizontalPath(startRow, startCol, endRow, endCol, False) == True):
            # Check lateral then forward and return 2
            if (self.checkVerticalPath(startRow, endCol, endRow, endCol, False) == True):
                return 2
        # Return -1 if no paths are clear
        return -1

    #    /* *********************************************************************
    #Function Name: getPath
    #Purpose: This function has two purposes depending on the execute parameter
    #1) If execute is false, simply check the path
    #2) If execute is true, the function executes the move to the end coordinates
    #Parameters:
    #	startX, startY, endX, endY, ints containing the start and end coordinates
    #	direction, int signifying the direction the piece will travel
    #	execute, a bool that determines if the function will actually move the die
    #Return Value:
    #	bool, return true at successful completion of path checking or path execution
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	player, string containing the player at the start coordinates
    #	endPlayer, string containing the player at the end coordinates
    #Algorithm:
    #1) If player = endPlayer, the move is invalid since the end space is occupied by
    #		a piece of the same player. Return false
    #2) If startX == endX, the path is strictly vertical
    #3)		If checkVerticalPath(...false) is true, the vertical path is clear. return true
    #4)			If execute is true and checkVerticalPath(...true) is true, move executed successfully
    #5) If startY == endY, repeat steps 3-4 with checkHorizontalPath instead
    #6) If direction == 1 check/execute vertical then horizontal path, return true if successful
    #7) If direction == 2 check/execute horizontal then vertical path, return true if successful
    #8) return false paths are not clear
    #Assistance Received: none
    #********************************************************************* */
    def getPath(self, startRow, startCol, endRow, endCol, direction, execute):
        tempBoard = self.boardObj.getGameBoard();
        player = tempBoard[startRow][startCol].getPlayer();
        endPlayer = tempBoard[endRow][endCol].getPlayer();

        # If endspace is occupied by Die of same player path is blocked
        if(player is endPlayer):
            return False;
        # If move is strictly vertical
        if(startCol == endCol):
            # If path is clear, execute move and return true
            if(self.checkVerticalPath(startRow, startCol, endRow, endCol, False) == True):
                if(execute == True):
                    if(self.checkVerticalPath(startRow, startCol, endRow, endCol, True) == True):
                        return True
                return True
            # If move is strictly horizontal
        elif (startRow == endRow):
            # If path is clear, execute move and return true
            if(self.checkHorizontalPath(startRow, startCol, endRow, endCol, False) == True):
                if(execute == True):
                    if(self.checkHorizontalPath(startRow, startCol, endRow, endCol, True) == True):
                        return True
                return True
            # If move is vertical then horizontal
        elif (direction == 1):
            # Check if path is clear
            if(self.checkVerticalPath(startRow, startCol, endRow, endCol, False) == True):
                if(self.checkHorizontalPath(endRow, startCol, endRow, endCol, False) == True):
                    if(execute == True):
                        # Execute Move
                        if(self.checkVerticalPath(startRow, startCol, endRow, endCol, True) == True):
                            if(self.checkHorizontalPath(endRow, startCol, endRow, endCol, True) == True):
                                return True
                    return True
          # If move is Horizontal then vertical
        elif(direction == 2):
            # Check if path is clear
            if(self.checkHorizontalPath(startRow, startCol, endRow, endCol, False) == True):
                if(self.checkVerticalPath(startRow, endCol, endRow, endCol, False) == True):
                    if(execute == True):
                        # Execute Move
                        if(self.checkHorizontalPath(startRow, startCol, endRow, endCol, True) == True):
                            if(self.checkVerticalPath(startRow, endCol, endRow, endCol, True) == True):
                                return True
                    return True
        # No clear Paths
        return False

    #    /* *********************************************************************
    #Function Name: getKeyPieceLoc
    #Purpose: Given the player find its opponent's keypiece
    #Parameters:
    #	player, string containing player who's executing the function
    #Return Value: vector<int> with vec[0] = x coord and vec[1] = y coord
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	location, vector<int> which is the return vector
    #Algorithm:
    #1) Loop through the board
    #2) if the current position contains an opponent's die and it's the keypiece
    #3)		push the x & y coord to location
    #4) return location
    #Assistance Received: none
    #********************************************************************* */
    def getKeypieceLoc(self, player):
        tempBoard = self.boardObj.getGameBoard()
        location = []
        for row in range(0, 8):
            for col in range(0, 9):
                if(player is "C"):
                    if(tempBoard[row][col].getPlayer() == "H" and tempBoard[row][col].getKeyPiece() == True):
                        location.append(row)
                        location.append(col)
                else:
                    if(tempBoard[row][col].getPlayer() == "C" and tempBoard[row][col].getKeyPiece() == True):
                        location.append(row)
                        location.append(col)
        return location

    #    /* *********************************************************************
    #Function Name: checkNumSpaces
    #Purpose: To check if start (x, y) is correct number of spaces from end (x, y)
    #			based off the top number of the starting piece
    #Parameters:
    #	startX & startY, integers containing the start X/Y positions
    #	endx & endY, integers containing the end X/Y positions
    #Return Value: bool, return true if they are the correct number of spaces away
    #Local Variables:
    #	vector<int> die, a temp holder for the positions of a die
    #	int move, takes the [0] index of die which is topNum == number of moves
    #	int tempX, tempY, tempXY, used to store the value of the start X/Y - endX/Y
    #		which shows us how many spaces they are from each other
    #Algorithm:
    #1) Fill in vector<int> die with the die from the [startY][startX] location on the gameboard
    #2) Set int move to the [0] location on the die
    #3) Subtract the end point by the starting point and take absolute value
    #4) Add together to get total number of spaces away
    #5) If number of moves allowed == number of spaces away --> return true
    #6) else return false
    #Assistance Received: none
    #********************************************************************* */
    def checkNumSpaces(self, startRow, startCol, endRow, endCol):
        tempBoard = self.boardObj.getGameBoard()
        die = tempBoard[startRow][startCol].getDie()
        # Get Number of moves allowed
        move = die[0]
        # Subtract the end point by the starting point and take absolute value
        # When added together it equals the total number of moves allowed
        tempRow = endRow - startRow
        tempCol = endCol - startCol
        tempRow = abs(tempRow)
        tempCol = abs(tempCol)
        tempRowCol = tempRow + tempCol
        if(tempRowCol == move):
            return True
        else:
            return False

    #/* *********************************************************************
    #Function Name: checkOccupiedSpace
    #Purpose: Check if the start coordinates contains a die of the correct player
    #Parameters:
    #x, y, two ints containing the start x/y coordinates
    #player, a string containing the player who called it
    #Local Variables: None
    #Algorithm:
    #1) Check if the gameboard is empty at [y][x]
    #2)		If true return false
    #3) If it's not empty check to make sure it's one of your pieces
    #4) Return true if its not empty and it is one of your Dies
    #Assistance Received: none
    #********************************************************************* */
    def checkOccupiedSpace(self, row, col, player):
        tempBoard = self.boardObj.getGameBoard()
        if (tempBoard[row][col].isEmpty() == True):
            return False
	    # Check if Player is moving correct Die
        elif (player != tempBoard[row][col].getPlayer()):
            return False
        return True

    #    /* *********************************************************************
    #Function Name: checkComputerWin
    #Purpose: return true if Computer win conditions are met
    #Parameters: None
    #Return Value: return true if Computer win conditions are met
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #Algorithm:
    #1) return true if the Human's keyspace is taken by the human key piece
    #2) return true if the vector returned by getKeypieceLoc is size 0
    #		this occurs when the opponents keypiece has been eliminated
    #Assistance Received: none
    #********************************************************************* */
    def checkComputerWin(self):
        tempBoardObj = self.getBoard()
        tempBoard = tempBoardObj.getGameBoard()
        location = self.getKeypieceLoc("C")
        # Check if the key square has been overtaken with keypiece
        if (tempBoard[0][4].getPlayer() == "C" and tempBoard[0][4].getKeyPiece() == True):
            return True
        # if len(location) == 0 there is no keypiece on the board
        elif (len(location) == 0):
            return True
        return False

    #    /* *********************************************************************
    #Function Name: checkHumanWin
    #Purpose: Check if Human player won the game
    #Parameters: None
    #Return Value: return true if Human win conditions are met
    #Local Variables:
    #		tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #Algorithm:
    #1) return true if the Computer's keyspace is taken by the human key piece
    #2) return true if the vector returned by getKeypieceLoc is size 0
    #		this occurs when the opponents keypiece has been eliminated
    #Assistance Received: none
    #********************************************************************* */
    def checkHumanWin(self):
        tempBoardObj = self.getBoard()
        tempBoard = tempBoardObj.getGameBoard()
        location = self.getKeypieceLoc("H")
        # Check if the key square has been overtaken with keypiece
        if (tempBoard[7][4].getPlayer() == "H" and tempBoard[7][4].getKeyPiece() == True):
            return True
        # if len(location) == 0 there is no keypiece on the board
        elif (len(location) == 0):
            return True
        return False

    #    /* *********************************************************************
    #Function Name: validateMove
    #Purpose: Function takes all the data about the pending move and prints 
    #			an error if it is not a legal move
    #Parameters:
    #	startX, startY, endX, endY, ints containing the start and end coordinates
    #	direction, int signifying the direction the piece will travel
    #	player, string containing the player
    #Return Value: return true if it's a legal move
    #Local Variables: None
    #Algorithm:
    #1) If startX and startY coordinates are out of bounds return false
    #2) If endX and endY coordinates are out of bound return false
    #3) If there's no valid piece on the space return false
    #4) If the start coordinates are not the correct number of moves away
    #from the end coordinates return false
    #5) If the path is blocked return false
    #6) return true
    #Assistance Received: none
    #********************************************************************* */
    def validateMove(self, startRow, startCol, endRow, endCol, direction, player):
    	# Check if starting coordinates are out of bounds
        if (self.checkOOB(startRow, startCol) == False):
            print("**************************************************")
            print("*  Error: Starting Coordinates Out of Bounds     *")
            print("*  Please Select New Coordinates                 *")
            print("**************************************************")
            return False
	    # Check if ending coordinates are out of bounds
        elif (self.checkOOB(endRow, endCol) == False):
            print("**************************************************")
            print("*  Error: Ending Coordinates Out of Bounds       *")
            print("*  Please Select New Coordinates                 *")
            print("**************************************************")
            return False
	    # Check if theres a valid die piece on the starting location
        elif (self.checkOccupiedSpace(startRow, startCol, player) == False):
            print("**************************************************")
            print("*  Error: No Valid Piece on Starting Coordinates *")
            print("*  Please Select New Coordinates                 *")
            print("**************************************************")
            return False
	    # Check if the end coordinates are the correct number of spaces 
	    # away from the starting coordinates
        elif (self.checkNumSpaces(startRow, startCol, endRow, endCol) == False):
            print("*****************************************************")
            print("*  Error: End Coordinates Out of Range of Movement  *")
            print("*  Please Select New Coordinates                    *")
            print("*****************************************************")
            return False
	    # Check if there are any pieces blocking move
        elif(self.getPath(startRow, startCol, endRow, endCol, direction, False) == False):
            print("*****************************************************")
            print("*  Error: Path is Blocked                           *")
            print("*  Please Select New Coordinates                    *")
            print("*****************************************************")
            return False
        return True

    #    /* *********************************************************************
    #Function Name: displayHelp
    #Purpose: Displays the help results for the human player
    #Parameters:
    #	startX, startY, endX, endY, ints containing the start and end coordinates
    #	direction, int signifying the direction the piece will travel
    #	moveType, string signifying the type of move to display
    #Return Value: void
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	message, a string containing message to display
    #Algorithm:
    #1) Depending on the moveType set the message to explain what the move will accomplish
    #2) Depending on the direction display the start die, the location, end location, and which direction to move first
    #Assistance Received: none
    #********************************************************************* */
    def displayHelp(self, startRow, startCol, endRow, endCol, direction, moveType):
        tempBoard = self.boardObj.getGameBoard()
        displayRow = startRow
        displayCol = startCol
        startRow += 1
        startCol += 1
        endRow += 1
        endCol += 1
        if (moveType == "attackPiece"):
            message = "To attack the key piece and win the game"
        elif (moveType == "attackSpace"):
            message = "To attack the key space and win the game"
        elif (moveType == "block"):
            message = "To perform blocking move                "
        elif (moveType == "overtake"):
            message = "To overtake a computer piece            "
        if (direction == 0):
            if (startCol == endCol):
                print("*******************************************************************************************************")
                print("*                                           ~~ Help ~~                                                *")
                print("*     " + message + "                                                        *")
                print("*     Choose die " + tempBoard[displayRow][displayCol].displayDie() + " at location (" + str(startRow) + "," + str(startCol) + ")                                                                *")
                print("*     Roll it to location (" + str(endRow) + "," + str(endCol) + ") frontally because it is the most direct clear path                    *")
                print("*******************************************************************************************************")
            else:
                print("*******************************************************************************************************")
                print("*                                           ~~ Help ~~                                                *")
                print("*     " + message + "                                                        *")
                print("*     Choose die " + tempBoard[displayRow][displayCol].displayDie() + " at location (" + str(startRow) + "," + str(startCol) + ")                                                                *")
                print("*     Roll it to location (" + str(endRow) + "," + str(endCol) + ") laterally because it is the most direct clear path          *")
                print("*******************************************************************************************************")
        elif (direction == 1):
                print("*******************************************************************************************************")
                print("*                                           ~~ Help ~~                                                *")
                print("*     " + message + "                                                        *")
                print("*     Choose die " + tempBoard[displayRow][displayCol].displayDie() + " at location (" + str(startRow) + "," + str(startCol) + ")                                                                *")
                print("*     Roll it to location (" + str(endRow) + "," + str(endCol) + ") frontally first because a frontal then lateral path is clear          *")
                print("*******************************************************************************************************")
        elif (direction == 2):
                print("*******************************************************************************************************")
                print("*                                           ~~ Help ~~                                                *")
                print("*     " + message + "                                                        *")
                print("*     Choose die " + tempBoard[displayRow][displayCol].displayDie() + " at location (" + str(startRow) + "," + str(startCol) + ")                                                                *")
                print("*     Roll it to location (" + str(endRow) + "," + str(endCol) + ") laterally first because a lateral then frontal path is clear          *")
                print("*******************************************************************************************************")

    #/* *********************************************************************
    #Function Name: displayMove
    #Purpose: Display the Computer's move and explain the reasoning behind it
    #Parameters:
    #	startX, startY, endX, endY, ints containing the start and end coordinates
    #	direction, int signifying the direction the piece will travel
    #	moveType, an int signifying the reason behind the move
    #Return Value: void
    #Local Variables:
    #	displayX/Y = used to hold the modifyable coordinates for display
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #Algorithm:
    #1) If moveType = 1, Display start die, coords, and key piece attack reasoning
    #2) If moveType = 2, Display start die, coords, and block attack reasoning
    #3) If moveType = 3, Display start die, coords, and overtake human die reasoning
    #4) If not 1, 2, or 3, Display start die, coords and last case reasoning
    #5) Then depending on the direction value
    #6) Calculate the number of spaces moved in a direction
    #7) Print the number of spaces moved in that direction and why it chose that path
    #Assistance Received: none
    #********************************************************************* */
    def displayMove(self, startRow, startCol, endRow, endCol, direction, moveType):
        tempBoard = self.boardObj.getGameBoard()
        displayRow = startRow
        displayCol = startCol
        displayEndRow = endRow
        displayEndCol = endCol
        displayRow += 1
        displayCol += 1
        displayEndRow += 1
        displayEndCol += 1
        if (moveType == 1):
		    # Display results for keypiece attack algorithm
            print("The Computer has Picked " + tempBoard[startRow][startCol].displayDie() + " at (" + str(displayRow) + "," + str(displayCol) + ") to roll to (" + str(displayEndRow) + "," + str(displayEndCol) + ") because this Die can win the game")
        elif (moveType == 2):
		    # Display results for keypiece block algorithm
            print("*The Computer has Picked " + tempBoard[startRow][startCol].displayDie() + " at (" + str(displayRow) + "," + str(displayCol) + ") to roll to (" + str(displayEndRow) + "," + str(displayEndCol) + ") because this Die can block an attack on the keypiece")
        elif (moveType == 3):
		    # Display results for overtake piece
            print("*The Computer has Picked " + tempBoard[startRow][startCol].displayDie() + " at (" + str(displayRow) + "," + str(displayCol) + ") to roll to (" + str(displayEndRow) + "," + str(displayEndCol) + ") because this Die can overtake a Human piece")
        else:
		    # Display results of best move algorithm
            print("The Computer has Picked " + tempBoard[startRow][startCol].displayDie() + " at (" + str(displayRow) + "," + str(displayCol) + ") to roll to (" + str(displayEndRow) + "," + str(displayEndCol) + ") because this Die can move closest to the Human KeyPiece")
	# Find type of roll and number of spaces for display
        if (direction == 0):
            if (startCol == endCol):
                numSpacesRow = abs(startRow - endRow)
                print("It rolled " + str(numSpacesRow) + " frontally because it was the most direct clear path")
            else:
                numSpacesCol = abs(startCol - endCol)
                print("It rolled " + str(numSpacesCol) + " laterally because it was the most direct clear path")
        elif (direction == 1):
            numSpacesRow = abs(startRow - endRow);
            numSpacesCol = abs(startCol - endCol);
            print("It rolled " + str(numSpacesRow) + " frontally and " + str(numSpacesCol) + " laterally because a frontal then lateral path was clear")
        elif (direction == 2):
            numSpacesRow = abs(startRow - endRow);
            numSpacesCol = abs(startCol - endCol);
            print("It rolled " + str(numSpacesCol) + " laterally and " + str(numSpacesRow) + " frontally because a straight frontal and frontal -> lateral move were blocked")



    ####################################################################
    #                           AI Functions                           #
    ####################################################################

    #    /* *********************************************************************
    #Function Name: keyPieceAttack
    #Purpose: First pass of AI algorithm
    #	Determines and excutes m a move overtaking the keypiece or keyspace
    #Parameters:
    #	player, string containing the player
    #	display, bool if true it will display help for human player
    #Return Value: return true if successful
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	KeyPieceLocation, vector<int> the vector holding the coords of the keypiece
    #	endX, endY, ints containing the coordinates of the keypiece
    #	direction, int signifying the direction the piece will travel
    #Algorithm:
    #1) Loop through each space on the board looking for a computer die
    #2) Check if that die is the correct number of spaces away from the end coords
    #3) Check if a move in any direction is clear
    #4) Display the chosen move and reasoning
    #5) Execute the move and return true
    #6) Do steps 1-5 except make the keyspace the end coords
    #7) If a human calls help()
    #8) Run steps 2-4 and display results for the human
    #Assistance Received: none
    #********************************************************************* */
    def keyPieceAttack(self, player, display):
        tempBoard = self.boardObj.getGameBoard()
        keyPieceLocation = self.getKeypieceLoc(player)
        endRow = keyPieceLocation[0]
        endCol = keyPieceLocation[1]

        for row in range(len(tempBoard)):
            for col in range(len(tempBoard[row])):
                if(player == "C"):
                    # If Die piece is a computer piece check all possible moves
                    # to either overtake the Human keypiece or the keyspace
                    if(tempBoard[row][col].getPlayer() == "C"):
                        # Check if the Computer Piece is the correct
                        # number of spaces from the Human Key Piece
                        if(self.checkNumSpaces(row, col, endRow, endCol) == True):
                            direction = self.getDirection(row, col, endRow, endCol)
                            #If direction != -1 path is clear in that direction
                            if(direction != -1):
                                self.displayMove(row, col, endRow, endCol, direction, 1);
                                # Execute move
                                if(self.getPath(row, col, endRow, endCol, direction, True)):
                                    return True;
                        elif (tempBoard[row][col].getKeyPiece() == True and self.checkNumSpaces(row, col, 0, 4) == True):
                            # Check against keyspace
                            direction = self.getDirection(row, col, 0, 4)
                            # If direction != -1 path is clear in that direction
                            if(direction != -1):
                                self.displayMove(row, col, 0, 4, direction, 1)
                                if(self.getPath(row, col, 0, 4, direction, True) == True):
                                    return True
                else:
                    # If Die piece is a human piece check all possible moves
                    # to either overtake the computer keypiece or the keyspace
                    if(tempBoard[row][col].getPlayer() == "H"):
                        # Check if the Computer Piece is the correct
                        # number of spaces from the Human Key Piece
                        if(self.checkNumSpaces(row, col, endRow, endCol) == True):
                            direction = self.getDirection(row, col, endRow, endCol)
                            if(direction != -1):
                                if(display == True):
                                    self.displayHelp(row, col, endRow, endCol, direction, "attackPiece")
                                return True
                        elif(tempBoard[row][col].getKeyPiece() == True and self.checkNumSpaces(row, col, 7, 4) == True):
                            # Check against keyspace
                            direction = self.getDirection(row, col, 7, 4);
                            # If direction != -1 path is clear in that direction
                            if(direction != -1):
                                if(display == True):
                                    self.displayHelp(row, col, 7, 4, direction, "attackSpace")
                                return True
        # Return false if no attack moves
        return False
    def executeBlock(self, endRow, endCol, execute):
        tempBoard = self.boardObj.getGameBoard()
        # Coordinates (endX, endY) is the Computer Keypiece
        # To find a candidate to block from below
        # find a Computer piece that can move to endX-- 
        for row in range(len(tempBoard)):
            for col in range(len(tempBoard[row])):
                if (execute == True):
                    if (tempBoard[row][col].getPlayer() == "C"):
                        if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                            direction = self.getDirection(row, col, endRow, endCol)
                            if (direction != -1):
                                self.displayMove(row, col, endRow, endCol, direction, 2)
                                if (self.getPath(row, col, endRow, endCol, direction, True) == True):
                                    return True
                else:
                    if (tempBoard[row][col].getPlayer() == "H"):
                        if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                            direction = self.getDirection(row, col, endRow, endCol)
                            if (direction != -1):
                                self.displayHelp(row, col, endRow, endCol, direction, "block")
                                return True
        # If there are no possible blocking moves return false
        return False

    #    /* *********************************************************************
    #Function Name: protectKeyPiece
    #Purpose: Second Pass of AI algorithm, move to protect keypiece
    #Parameters:
    #	player, string containing the player
    #	keySpace, bool if true it will block keyspace
    #Return Value: return true if successful
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	KeyPieceLocation, vector<int> the vector holding the coords of the keypiece
    #	endX, endY, ints containing the coordinates of the keypiece
    #	direction, int signifying the direction the piece will travel
    #Algorithm:
    #1) Set the end coords based on player and if they're checking the keyspace or keypiece
    #2) Loop through each space of the board looking for an opponents die
    #3) Check if that die is the correct number of moves away from your keyPiece/Space
    #4) Check if any path is clear to the end space meaning you're vulnerable for attack
    #5) Depending on the direction call executeBlock on the proper end coordinates
    #		to check if any of the players pieces can block
    #Assistance Received: none
    #********************************************************************* */
    def protectKeyPiece(self, player, keySpace):
        tempBoard = self.boardObj.getGameBoard()

        # If its a computer move and we're trying to protect the key piece
        if(player == "C" and keySpace == False):
            keyPieceLocation = self.getKeypieceLoc("H")
            endRow = keyPieceLocation[0]
            endCol = keyPieceLocation[1]
        elif(player == "C" and keySpace == True):
            # If its a computer move and we're trying to protect the key space
            endRow = 7
            endCol = 4
        elif (player == "H" and keySpace == False):
            # If its a human move and we're trying to protect the key piece
            keyPieceLocation = self.getKeypieceLoc("C")
            endRow = keyPieceLocation[0]
            endCol = keyPieceLocation[1]
        else:
            # If its a human move and we're trying to protect the key space
            endRow = 0
            endCol = 4

        for row in range(len(tempBoard)):
            for col in range(len(tempBoard[row])):
                # Computer Move
                if(player == "C"):
                    # If Die piece is a human piece check all possible moves
                    # that can overtake the computer keypiece or the keyspace
                    if (tempBoard[row][col].getPlayer() == "H"):
                        # Check if the Human Piece is the correct
                        # number of spaces from the Computer Key Piece
                        if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                            direction = self.getDirection(row, col, endRow, endCol)
                            # If check path is true, then Human has a winning move
                            # Execute block and return true
                            if (direction != -1):
                                if (direction == 0):
                                    # If its a vertical attack and end is higher than start
                                    if (col == endCol and endRow > row):
                                        endRow -= 1
                                        # For a forward attack set --endY
                                        # So block manuever is executed one space below keypiece
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True
                                    # If its a vertical attack and end is lower than start
                                    elif (col == endCol and endRow < row):
                                        endRow += 1
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True;
                                    # If its a Horizontal attack and end is higher than start
                                    elif (row == endRow and endCol > col):
                                        # Block Space to left of Keypiece
                                        if (endCol > col):
                                            endCol -= 1
                                            if (self.executeBlock(endRow, endCol, True) == True):
                                                return True
                                    # If its a Horizontal attack and end is lower than start
                                    elif (row == endRow and endCol < col):
                                        endCol += 1
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True;
                                # If its a forward -> lateral attack
                                elif (direction == 1):
                                    # Block Space to left of Keypiece
                                    if (endCol > col):
                                        endCol -= 1
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True
                                    elif (endCol < col):
                                        endCol += 1
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True
                                # If its a lateral -> forward
                                elif (direction == 2):
                                    if (endRow > row):
                                        endRow -= 1
                                        # For a forward or lateral->forward attack set --endY
                                        # So block manuever is executed one space below keypiece
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True
                                    elif (endRow < row):
                                        endRow += 1
                                        if (self.executeBlock(endRow, endCol, True) == True):
                                            return True;
                # Human Move
                else:
                    # If Die piece is a Computer piece check all possible moves
                    # that can overtake the human keypiece or the keyspace
                    if (tempBoard[row][col].getPlayer() == "C"):
                        # Check if the Computer Piece is the correct
                        # number of spaces from the Human Key Piece
                        if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                            direction = self.getDirection(row, col, endRow, endCol)
                            # If check path is true, then Human has a winning move
                            # Execute block and return true
                            if (direction != -1):
                                if (direction == 0):
                                    # If its a vertical attack and end is higher than start
                                    if (col == endCol and endRow > row):
                                        endRow -= 1
                                        # For a forward attack set --endY
                                        # So block manuever is executed one space below keypiece
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
                                    # If its a vertical attack and end is lower than start
                                    elif (col == endCol and endRow < row):
                                        endRow += 1
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
                                    # If its a Horizontal attack and end is higher than start
                                    elif (row == endRow and endCol > col):
                                        # Block Space to left of Keypiece
                                        if (endCol > col):
                                            endCol -= 1
                                            if (self.executeBlock(endRow, endCol, False) == True):
                                                return True
                                    # If its a Horizontal attack and end is lower than start
                                    elif (row == endRow and endCol < col):
                                        endCol += 1
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
                                # If its a forward -> lateral attack
                                elif (direction == 1):
                                    # Block Space to left of Keypiece
                                    if (endCol > col):
                                        endCol -= 1
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
                                    elif (endCol < col):
                                        endCol += 1
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
                                # If its a lateral -> forward
                                elif (direction == 2):
                                    if (endRow > row):
                                        endRow -= 1
                                        # For a forward or lateral->forward attack set --endY
                                        # So block manuever is executed one space below keypiece
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
                                    elif (endRow < row):
                                        endRow += 1
                                        if (self.executeBlock(endRow, endCol, False) == True):
                                            return True
        return False

    #    /* *********************************************************************
    #Function Name: checkOvertake
    #Purpose: Third pass of AI algorithm, Check if theres a die to overtake
    #Parameters:
    #	player, string containing the player
    #Return Value: return true if successful overtake
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	direction, int signifying the direction the piece will travel
    #Algorithm:
    #1) Loop through board looking for a die owned by player
    #2) Once found, loop through board again looking for die owned by opponent
    #3) Check the distance between the two die
    #4) Find a direction with a clear path 
    #5) Execute move and overtake piece
    #Assistance Received: none
    #********************************************************************* */
    def checkOvertake(self, player):
        tempBoard = self.boardObj.getGameBoard()
        for row in range(len(tempBoard)):
            for col in range(len(tempBoard[row])):
                # Computer Move
                if (player == "C"):
                    # If Die piece is a computer piece check all possible moves
                    # to overtake a Human Piece
                    if (tempBoard[row][col].getPlayer() == "C"):
                        for endRow in range(0, 8):
                            for endCol in range(0, 9):
                                if (tempBoard[endRow][endCol].getPlayer() == "H"):
                                    if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                                        direction = self.getDirection(row, col, endRow, endCol)
                                        if (direction != -1):
                                            self.displayMove(row, col, endRow, endCol, direction, 3)
                                            if (self.getPath(row, col, endRow, endCol, direction, True) == True):
                                                return True
                # Human move
                else:
                    # If Die piece is a Human piece check all possible moves
                    # to overtake a Computer Piece
                    if (tempBoard[row][col].getPlayer() == "H"):
                        for endRow in range(7, -1, -1):
                            for endCol in range(0, 9):
                                if (tempBoard[endRow][endCol].getPlayer() == "C"):
                                    if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                                        direction = self.getDirection(row, col, endRow, endCol)
                                        if (direction != -1):
                                            self.displayHelp(row, col, endRow, endCol, direction, "overtake")
                                            return True
        return False

    #    /* *********************************************************************
    #Function Name: executeBlock
    #Purpose: If it is found an opponent can attack, check for a possible candidate to block
    #Parameters:
    #	endX, endY, ints containing the end coordinates
    #	bool, true if function should execute the move
    #Return Value: return true if successful
    #Local Variables:
    #	tempBoard, vector<vector<Die>> which is filled with the current state of the board
    #	direction, int signifying the direction the piece will travel
    #Algorithm:
    #1) Loop through board looking for one of your own die
    #2) Check to see if the piece is the correct distance from the end space
    #3) Get a direction with a clear path
    #4) Display the move
    #5) Execute move
    #6) Do steps 1-4 if Human is player
    #7) Send data to the help function
    #Assistance Received: none
    #********************************************************************* */
    def executeBestMove(self):
        tempBoard = self.boardObj.getGameBoard()
        keyPieceLocation = self.getKeypieceLoc("C")
        keyRow = keyPieceLocation[0]
        keyCol = keyPieceLocation[1]
        score = 100
        direction = -1
        # Loop through board finding every C piece
        for row in range(0, 8):
            for col in range(0, 9):
                if (tempBoard[row][col].getPlayer() == "C"):
                    # When C piece is found loop through board again
                    # Checking all possible end locations
                    for endRow in range(0, 8):
                        for endCol in range(0, 9):
                            # If end point is proper number of spaces
                            # Check path and get direction and calculate score
                            if (self.checkNumSpaces(row, col, endRow, endCol) == True):
                                tempDirection = self.getDirection(row, col, endRow, endCol)
                                # If getDirection != -1 path is clear
                                if (tempDirection != -1):
                                    tempScore = (abs(endCol - keyCol) + abs(endRow - keyRow))
                                    if (tempScore < score):
                                        score = tempScore
                                        direction = tempDirection
                                        startRow = row
                                        startCol = col
                                        finalRow = endRow
                                        finalCol = endCol
        self.displayMove(startRow, startCol, finalRow, finalCol, direction, 4)
        # If move is executed return true;
        return self.getPath(startRow, startCol, finalRow, finalCol, direction, True)

    #    /* *********************************************************************
    #Function Name: help
    #Purpose: This function calls all the AI components as a human player
    #			to generate the help prompts
    #Parameters: None
    #Return Value: void
    #Local Variables: None
    #Algorithm:
    #1) Check if a human die can attack the computer's keypiece
    #2) Check if a human die can defend the keypiece
    #3) Check if a human die can defend the keyspace
    #4) Check is a human die can overtake a computer die
    #5) If none of these scenarios are true, prompt the player to move any piece they choose
    #Assistance Received: none
    #********************************************************************* */
    def help(self):
	    # Check if Human has winning move
        if (self.keyPieceAttack("H", True) == True):
            print()
        elif (self.protectKeyPiece("H", False) == True):
            print()
        elif (self.protectKeyPiece("H", True) == True):
            print()
        elif (self.checkOvertake("H") == True):
            print()
        else:
            print("***********************************************************************************")
            print("*                               ~~ Help ~~                                        *")
            print("*     There are no critical moves to execute, move any die of your choosing       *")
            print("***********************************************************************************")

