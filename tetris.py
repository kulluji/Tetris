import random

class Piece:
    def __init__(self):
        self.pieces = [
            [['*','*','*','*']],

            [['*',' '],
             ['*',' '],
             ['*','*']],

            [[' ','*'],
             [' ','*'],
             ['*','*']],

            [['*','*'],
             ['*','*']]

        ]
    

    def pickRanndomPiece(self):
        return random.choice(self.pieces)
    

    @staticmethod
    def rotate_piece_clockwise(piece):
    
        rows = len(piece)
        cols = len(piece[0])

        new_piece = []
        for _ in range(cols):
            new_piece.append([" "] * rows)
        for i in range(rows):
            for j in range(cols):
                new_piece[j][rows-1-i] = piece[i][j]
        return new_piece
    
    @staticmethod
    def rotate_piece_counter_clockwise(piece):
        # Get the height and width of the piece
        rows = len(piece)
        cols = len(piece[0])

        # Create a new empty piece with the dimensions swapped
        new_piece = []
        for _ in range(cols):
            new_piece.append([" "] * rows)

        # Copy the values from the old piece to the new piece in reverse order
        for x in range(cols):
            for y in range(rows):
                new_piece[x][y] = piece[y][cols - x - 1]

        return new_piece
    
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

board = Board(12,12)
piece = Piece()

class Tetris:
    
    
    def checkIfAnyValidMove(self):
    
        clockwise_piece = piece.rotate_piece_clockwise(self.current_piece)
        counter_clockwise_piece = piece.rotate_piece_counter_clockwise(self.current_piece)

        # Four actions that we can perform

        if board.isValidMove(self.current_piece, self.current_row + 1,  self.current_col - 1):
            return True
        
        if board.isValidMove(self.current_piece, self.current_row + 1,  self.current_col + 1):
            return True
        
        if board.isValidMove(clockwise_piece, self.current_row + 1,  self.current_col):
            return True
        
        if board.isValidMove(counter_clockwise_piece, self.current_row + 1,  self.current_col):
            return True
        
        return False
    
    def checkAndPlaceNewPiece(self):
        self.current_piece = piece.pickRanndomPiece()
        self.current_row = 0
        self.current_col = random.randint(0, 11 - len(self.current_piece[0]))
        if(board.isValidMove(self.current_piece,self.current_row,self.current_col)):
            board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')
            return True
        else:
            return False

    def start(self):
        self.current_piece = piece.pickRanndomPiece()
        self.current_row = 0
        self.current_col = 4
        
        # place the first piece on the board
        board.updateBoard(self.current_piece, self.current_row, self.current_col, '*')

        while(True):
            
            board.printBoard()
                
            action = input('Enter the action you want to perform : ')
            print('Your action',action)
            if(action == 'a'):
                
                # remove the current piece from the board
                board.updateBoard(self.current_piece,self.current_row,self.current_col,' ')

                # check if the new position where piece is placed is valid or not
                if(board.isValidMove(self.current_piece,self.current_row + 1,self.current_col - 1)):

                    # update the board with new position
                    board.updateBoard(self.current_piece,self.current_row + 1, self.current_col - 1,'*')

                    self.current_row  = self.current_row + 1
                    self.current_col  = self.current_col - 1
                    continue
                elif not board.isValidMove(self.current_piece,self.current_row + 1,self.current_col - 1):
                    if not self.checkIfAnyValidMove():

                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')

                        # pick a new piece randomly and check if the new piece can be placed on the board
                        if not self.checkAndPlaceNewPiece():
                            break
                        else:
                            print('New Piece is placed on the board')
                    else:
                        print("This action is not valid but you can enter other actions")
                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')
                    

            elif(action == 'd'):

                board.updateBoard(self.current_piece,self.current_row,self.current_col,' ')
                if(board.isValidMove(self.current_piece,self.current_row + 1,self.current_col + 1)):
                    board.updateBoard(self.current_piece,self.current_row + 1, self.current_col + 1,'*')
                    self.current_row  = self.current_row + 1
                    self.current_col  = self.current_col + 1
                    continue
                elif not board.isValidMove(self.current_piece,self.current_row + 1,self.current_col + 1):
                    if not self.checkIfAnyValidMove():

                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')

                        # pick a new piece randomly and check if the new piece can be placed on the board
                        if not self.checkAndPlaceNewPiece():
                            break
                        else:
                            print('New Piece is placed on the board')
                    else:
                        print("This action is not valid but you can enter other actions")
                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')
            elif(action == 'w'):
                
                board.updateBoard(self.current_piece,self.current_row,self.current_col,' ')
                new_piece = piece.rotate_piece_counter_clockwise(self.current_piece)
                if(board.isValidMove(new_piece,self.current_row + 1,self.current_col)):
                    
                    board.updateBoard(new_piece,self.current_row + 1, self.current_col,'*')
                    self.current_piece = new_piece
                    self.current_row  = self.current_row + 1
                    continue
                elif not board.isValidMove(new_piece,self.current_row + 1,self.current_col):
                    if not self.checkIfAnyValidMove():

                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')

                        # pick a new piece randomly and check if the new piece can be placed on the board
                        if not self.checkAndPlaceNewPiece():
                            break
                        else:
                            print('New Piece is placed on the board')
                    else:
                        print("This action is not valid but you can enter other actions")
                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')

            elif(action == 's'):

                board.updateBoard(self.current_piece,self.current_row,self.current_col,' ')
                new_piece = piece.rotate_piece_clockwise(self.current_piece)
                if(board.isValidMove(new_piece,self.current_row + 1,self.current_col)):

                    board.updateBoard(new_piece,self.current_row + 1, self.current_col,'*')
                    self.current_piece = new_piece
                    self.current_row  = self.current_row + 1
                    continue
                elif not board.isValidMove(new_piece,self.current_row + 1,self.current_col):
                    if not self.checkIfAnyValidMove():

                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')

                        # pick a new piece randomly and check if the new piece can be placed on the board
                        if not self.checkAndPlaceNewPiece():
                            break
                        else:
                            print('New Piece is placed on the board')
                    else:
                        print("This action is not valid but you can enter other actions")
                        # place the piece back at the same position
                        board.updateBoard(self.current_piece,self.current_row,self.current_col,'*')
                
            else:
                print('You have entered an invalid action, please enter a valid action')
                continue

        print('Game Over!')
            






tetris  = Tetris()
tetris.start()