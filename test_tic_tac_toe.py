import unittest
from parameterized import parameterized
import app.tic_tac_toe


class TestTicTacToe(unittest.TestCase):
    def setUp(self) -> None:
        self.tic_tac_toe = app.tic_tac_toe.TicTacToe()

    # Kiedy ktoś umieści znak poza osią X, program powinien zgłosić RuntimeError
    def test_whenXOutsideBoardThenRuntimeError(self):
        with self.assertRaises(RuntimeError):
            self.tic_tac_toe.play(4, 2)

    # Kiedy ktoś umieści znak poza osią Y, program powinien zgłosić RuntimeError
    def test_whenYOutsideBoardThenRuntimeError(self):
        with self.assertRaises(RuntimeError):
            self.tic_tac_toe.play(2, 4)

    # Kiedy ktoś umieści znak w zajętym polu, program powinien zwrócić RuntimeError
    def test_whenOccupiedThenRuntimeError(self):
        self.tic_tac_toe.play(2, 1)
        with self.assertRaises(RuntimeError):
            self.tic_tac_toe.play(2, 1)

    # Pierwszą turę powinien rozgrywać gracz X
    def test_givenFirstTurnWhenNextPlayerThenX(self):
        self.assertEqual('X', self.tic_tac_toe.next_player())

    # Jeśli ostatnia tura była rozegrana przez X, O powinien rozegrać kolejną turę
    def test_givenLastTurnWasXWhenNextPlayerThenO(self):
        self.tic_tac_toe.play(1, 1)
        self.assertEqual('O', self.tic_tac_toe.next_player())

    # Jeśli ostatnia tura była rozegrana przez O, X powinien rozegrać kolejną turę.
    def test_givenLastTurnWasOWhenNextPlayerThenX(self):
        self.tic_tac_toe.play(1, 1)
        self.tic_tac_toe.play(2, 2)
        self.assertEqual('X', self.tic_tac_toe.next_player())

    def test_whenPlayThenNoWinner(self):
        actual = self.tic_tac_toe.play(1, 1)
        self.assertEqual("No winner", actual)

    def test_whenPlayAndWholeHorizontalLineThenWinner(self):
        self.tic_tac_toe.play(1, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(2, 1)  # X
        self.tic_tac_toe.play(2, 2)  # O
        actual = self.tic_tac_toe.play(3, 1)  # X
        self.assertEqual("X is the winner", actual)

    def test_whenPlayAndWholeVerticalLineThenWinner(self):
        self.tic_tac_toe.play(2, 1)  # X
        self.tic_tac_toe.play(1, 1)  # O
        self.tic_tac_toe.play(3, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(2, 2)  # X
        actual = self.tic_tac_toe.play(1, 3)  # O
        self.assertEqual("O is the winner", actual)

    def test_whenPlayAndTopBottomDiagonalLineThenWinner(self):
        self.tic_tac_toe.play(1, 1)  # X
        self.tic_tac_toe.play(1, 2)  # O
        self.tic_tac_toe.play(2, 2)  # X
        self.tic_tac_toe.play(1, 3)  # O
        actual = self.tic_tac_toe.play(3, 3)  # X
        self.assertEqual("X is the winner", actual)

    def test_whenPlayAndTopBottomInvertedDiagonalLineThenWinner(self):
        self.tic_tac_toe.play(1, 3)
        self.tic_tac_toe.play(2, 1)
        self.tic_tac_toe.play(2, 2)
        self.tic_tac_toe.play(3, 3)
        actual = self.tic_tac_toe.play(3, 1)
        self.assertEqual("X is the winner", actual)

    def test_whenDraw(self):
        self.tic_tac_toe.play(1, 1)
        self.tic_tac_toe.play(2, 1)
        self.tic_tac_toe.play(3, 1)
        self.tic_tac_toe.play(1, 2)
        self.tic_tac_toe.play(2, 2)
        self.tic_tac_toe.play(1, 3)
        self.tic_tac_toe.play(3, 2)
        self.tic_tac_toe.play(3, 3)
        actual = self.tic_tac_toe.play(2, 3)
        self.assertEqual('No winner', actual)

    @parameterized.expand([
        ["whole_horizontal", [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1)], "X is the winner"],
        ["whole_vertical", [(2,1),(1,1),(3,1),(1,2),(3,2),(1,3)], "O is the winner"]
    ])
    def test_alot(self, name, moves: list, results: str):
        for move in range(len(moves) - 1):
            self.tic_tac_toe.play(moves[move][0], moves[move][1])
        actual = self.tic_tac_toe.play(moves[-1][0], moves[-1][1])
        self.assertEqual(results, actual)
    @parameterized.expand([
        ['outside_X',4,2],
        ['outside_Y',2,4]
    ])
    def test_raisesalot(self,name,x,y):
        with self.assertRaises(RuntimeError):
            self.tic_tac_toe.play(x,y)