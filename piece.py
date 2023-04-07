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