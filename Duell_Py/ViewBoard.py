#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
class ViewBoard():
    """Print the gameboard"""
    #    /* *********************************************************************
    #Function Name: displayBoard
    #Purpose: Display the board
    #Parameters: list of list of die objects gameboard by reference
    #Return Value: void
    #Algorithm:
    #1) Loop through gameboard 
    #2) Print each index
    #3) Print the x and y indexes
    #Assistance Received: none
    #********************************************************************* */
    def displayBoard(self, tempboard):
        rowIndex = 8
        for row in range (7, -1, -1):
            print("  +---+---+---+---+---+---+---+---+---+")
            print(rowIndex, end=" ")
            for col in range(0, 9):
                if(tempboard[row][col].displayDie() == "00"):
                    print("|   ", end="")
                else:
                    print("|" + tempboard[row][col].displayDie(), end="")
            rowIndex -= 1
            print("|")
        print("  +---+---+---+---+---+---+---+---+---+")
        print("    ", end="")
        for i in range(1, 10):
            print(i, end="   ") 
        print()


