import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(12, 12)

    def test_updateBoard(self):
        piece = [['*','*'],
                 ['*','*']]
        expected_board = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ','*','*',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ','*','*',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        self.board.updateBoard(piece, 8, 4, '*')
        self.assertEqual(self.board.array, expected_board)

    def test_isValidMove(self):
        piece = [['*','*'],
                 ['*','*']]
        self.assertTrue(self.board.isValidMove(piece, 0, 4))
        self.assertFalse(self.board.isValidMove(piece, 0, 11))

if __name__ == '__main__':
    unittest.main()