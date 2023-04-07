class Board:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.array = [[" " for j in range(self.columns)] for i in range(self.rows)]
    

    def printBoard(self):
        for row in self.array:
            print(row)
        
    def getCurrentStateOfBoard(self):
        return self.array
    
    def updateBoard(self,piece,row,column,symbol):
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                if(piece[i][j] == '*'):
                    self.array[row+i][column+j] = symbol

        return True
    def isValidMove(self,piece,row,column):
        for i in range(len(piece)):
            for j in range(len(piece[i])):

                if(row + i >= 12 or column + j < 0 or column + j >= 12):
                    return False
                elif(piece[i][j] == '*' and self.array[row+i][column+j] == '*'):
                    return False
        return True