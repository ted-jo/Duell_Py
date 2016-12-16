#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
class Die(object):
    """Die Object"""
    def __init__(self):
        self.player = ""
        self.keypiece = False
        self.die = [0] * 6
    # Setters
    def setDie(self, newDie):
        self.die = newDie
    def setPlayer(self, newPlayer):
        self.player = newPlayer
    def setKeyPiece(self, kp):
        self.keypiece = kp
    # Getters
    def getDie(self):
        return self.die
    def getPlayer(self):
        return self.player
    def getKeyPiece(self):
        return self.keypiece

    #    /* *********************************************************************
    #Function Name: displayDie
    #Purpose: Display the die in format P12
    #Parameters: None
    #Return Value: String with the player, top and right side
    #Assistance Received: none
    #********************************************************************* */
    def displayDie(self):
        return (self.player + str(self.die[0]) + str(self.die[3]))

    #    /* *********************************************************************
    #Function Name: isEmpty
    #Purpose: Check if die is empty
    #Parameters: None
    #Return Value: return true if die is empty
    #Assistance Received: none
    #********************************************************************* */
    def isEmpty(self):
        return self.die[0] == 0

    #    /* *********************************************************************
    #Function Name: frontalMove
    #Purpose: Swap die faces to move forward by one space
    #Parameters: None
    #Return Value: void
    #Assistance Received: none
    #********************************************************************* */
    def frontalMove(self):
        # Die[top, bottom, left, right, front, back]
	    # newDie[back, front, left, right, top, bottom]
        newDie = [0] * 6
        newDie[0] = self.die[5]
        newDie[1] = self.die[4]
        newDie[2] = self.die[2]
        newDie[3] = self.die[3]
        newDie[4] = self.die[0]
        newDie[5] = self.die[1]
        self.setDie(newDie)

    #    /* *********************************************************************
    #Function Name: backwardMove
    #Purpose: Swap die faces to move backward by one space
    #Parameters: None
    #Return Value: void
    #Assistance Received: none
    #********************************************************************* */
    def backwardMove(self):
        # Die[top, bottom, left, right, front, back]
	    # newDie[front, back, left, right, bottom, top]
        newDie = [0] * 6
        newDie[0] = self.die[4]
        newDie[1] = self.die[5]
        newDie[2] = self.die[2]
        newDie[3] = self.die[3]
        newDie[4] = self.die[1]
        newDie[5] = self.die[0]
        self.setDie(newDie)

    #    /* *********************************************************************
    #Function Name: lateralLeftMove
    #Purpose: Swap die faces to move left by one space
    #Parameters: None
    #Return Value: void
    #Assistance Received: none
    #********************************************************************* */
    def lateralLeftMove(self):
        # Die[top, bottom, left, right, front, back]
	    # newDie[right, left, top, bottom, front, back]
        newDie = [0] * 6
        newDie[0] = self.die[3]
        newDie[1] = self.die[2]
        newDie[2] = self.die[0]
        newDie[3] = self.die[1]
        newDie[4] = self.die[4]
        newDie[5] = self.die[5]
        self.setDie(newDie)

    #    /* *********************************************************************
    #Function Name: lateralRightMove
    #Purpose: Swap die faces to move right by one space
    #Parameters: None
    #Return Value: void
    #Assistance Received: none
    #********************************************************************* */
    def lateralRightMove(self):
        # Die[top, bottom, left, right, front, back]
	    # newDie[left, right, bottom, top, front, back]
        newDie = [0] * 6
        newDie[0] = self.die[2]
        newDie[1] = self.die[3]
        newDie[2] = self.die[1]
        newDie[3] = self.die[0]
        newDie[4] = self.die[4]
        newDie[5] = self.die[5]
        self.setDie(newDie)