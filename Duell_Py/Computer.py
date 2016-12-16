#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
from Player import Player
class Computer(Player):
    """Computer Class: Executes AI functions"""
    #    /* *********************************************************************
    #Function Name: play
    #Purpose: Virtual function that executes the AI move
    #Parameters: None
    #Return Value: Pointer to a board object
    #Local Variables: None
    #Algorithm:
    #1) Check if AI can attack keypiece
    #2) Check if AI can block a keypiece attack
    #3) Check if AI can block a keyspace attack
    #4) Check if AI can overtake a piece
    #5) Check if AI can execute best move available
    #6) return the boardObj
    #Assistance Received: none
    #********************************************************************* */
    def play(self):
        print()
        print("****************************************************************************************************")
        print("                 It's the Computer's Turn!")
        if(self.keyPieceAttack("C", False) == True):
           print("The Computer Has Attacked Your KeyPiece")
        elif(self.keyPieceAttack("H", False) == True and self.protectKeyPiece("C", False) == True):
            print("Human has a finishing move on key piece, Initiate block")
        elif(self.keyPieceAttack("H", False) == True and self.protectKeyPiece("C", True) == True):
            print("Human has finishing move on key space, Initiate block")
        elif(self.checkOvertake("C") == True):
            print("Computer executed a move to overtake a human die")
        elif(self.executeBestMove() == True):
            print("Computer executed best possible move")
        print("****************************************************************************************************")
        return self.boardObj



