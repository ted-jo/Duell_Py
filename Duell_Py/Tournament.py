#************************************************************
#* Name:  Ted Johansmeyer                                   *
#* Project : Python Duell                                   *
#* Class : CMPS 366 Organization of Programming Languages   *
#* Date : December 13th 2016                                *
#************************************************************
class Tournament(object):
    """Tournament Class: Holds the wins for each player"""
    def __init__(self):
        self.computerWins = 0
        self.humanWins = 0
    # Getters
    def getComputerWins(self):
        return self.computerWins
    def getHumanWins(self):
        return self.humanWins
    # Setters
    def setComputerWins(self, compWins):
        if(compWins >= 0):
            self.computerWins = compWins
    def setHumanWins(self, humWins):
        if(humWins >= 0):
            self.humanWins = humWins


