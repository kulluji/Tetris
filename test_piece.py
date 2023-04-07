import unittest
from piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.piece = Piece()

    def test_pickRandomPiece(self):
        pieces = [
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
        self.assertIn(self.piece.pickRanndomPiece(), pieces)

    def test_rotate_piece_clockwise(self):
        piece = [['*','*'],
                 ['*',' ']]
        expected_piece = [['*','*'],
                          [' ','*']]
        self.assertEqual(Piece.rotate_piece_clockwise(piece), expected_piece)

    def test_rotate_piece_counter_clockwise(self):
        piece = [['*','*'],
                 ['*',' ']]
        expected_piece = [[' ','*'],
                          ['*','*']]
        self.assertNotEqual(Piece.rotate_piece_counter_clockwise(piece), expected_piece)


if __name__ == '__main__':
    unittest.main()

