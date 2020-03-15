from string import ascii_lowercase

class Board():
    
    def __init__(self, rows, columns):

        def createFieldDictinary(rows, columns):
            fieldDictinary = dict()
            for row in range(rows):
                for col in range(columns):
                    
                    letterStr = ascii_lowercase[col]
                    numberStr = str(row+1)
                    name = letterStr + numberStr

                    position = tuple([row,col])
                    fieldDictinary.update({name: position})
            return fieldDictinary
        
        self.rows = rows
        self.columns = columns
        self.fieldDictinary = createFieldDictinary(self.rows, self.columns)    
        self.fields = [Field(name, position) for name, position in self.fieldDictinary.items()]
        
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
    
    def __init__(self, name, position, stone=None):
        self.name = name
        self.position = position
        self.stone = stone

    def __str__(self):
        return "Name: {self.name}\nPosition: {self.position} \n".format(self=self)

    def addStone(self, stone):
        pass

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

if __name__ == "__main__":
    board = Board(8,8)
    print(board.fields[1])