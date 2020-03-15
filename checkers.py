class Board():
    
    def __init__(self):
        self.rows = rows
        self.columns = columns
        self.grid = grid

    def getEmptyFields(self):
        pass

    def getOccupiedFields(self):
        #returns list of (x,y) tuples
        pass

    def getNumberOfStones(self, color='all'):
        pass

    def printBoard(self):
        pass

class Field():
    
    def __init__(self):
        self.name = name
        self.position = position

    def isEmpty(self):
        pass

    def isOccupied(self):
        pass

class Stone():
    
    def __init__(self, color, position, isQueen):
        self.color = color
        self.position = position
        self.isQueen = isQueen

    def possibleMoves(self):
        pass

    def moveTo(self):
        pass

    def isJumped(self):
        pass

    def remove(self):
        pass

    def becomeQueen(self):
        pass


