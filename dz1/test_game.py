"""The test game module"""

import unittest
import game


class TestGame(unittest.TestCase):

    """Test game class"""

    def setUp(self):
        self.player_a = 'A'
        self.player_b = 'B'
        self.tic_tac = game.TicTacGame(self.player_a, self.player_b)

    def test_win(self):

        """Test win method"""

        self.tic_tac.start(msg=False)
        self.tic_tac.turn(self.player_a, 0, 0)
        self.tic_tac.turn(self.player_a, 1, 1)
        self.tic_tac.turn(self.player_a, 2, 2)
        self.assertEqual(self.tic_tac.get_winner(), self.player_a)

    def test_draw(self):

        """Test draw method"""

        self.tic_tac.start(msg=False)
        self.tic_tac.turn(self.player_a, 0, 1)
        self.tic_tac.turn(self.player_a, 0, 0)
        self.tic_tac.turn(self.player_a, 1, 2)
        self.tic_tac.turn(self.player_a, 2, 0)

        self.tic_tac.turn(self.player_b, 0, 2)
        self.tic_tac.turn(self.player_b, 1, 0)
        self.tic_tac.turn(self.player_b, 1, 1)
        self.tic_tac.turn(self.player_b, 2, 1)
        self.tic_tac.turn(self.player_b, 2, 2)

        self.assertEqual(self.tic_tac.get_winner(), f"{self.player_a} and {self.player_b}")

    def test_none_win(self):

        """Test draw method"""

        self.tic_tac.start(msg=False)
        self.tic_tac.turn(self.player_a, 0, 1)
        self.tic_tac.turn(self.player_b, 0, 0)
        self.tic_tac.turn(self.player_a, 1, 2)
        self.tic_tac.turn(self.player_b, 2, 0)

        self.assertEqual(self.tic_tac.get_winner(), None)
