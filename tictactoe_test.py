import unittest
from tictactoe import Game


class TicTacToeTest(unittest.TestCase):
    def test_always_true(self):
        self.assertTrue(True)

    def test_should_have_empty_board_when_init_the_game(self):
        game = Game()

        self.assertEqual(game.board, ["_", "_", "_", "_", "_", "_", "_", "_", "_"])

    def test_should_be_X_turn_when_start_the_game(self):
        game = Game()

        game.start()

        self.assertEqual(game.turn, "X")

    def test_should_block_0_is_X_when_X_play_at_0(self):
        game = Game()

        game.start()
        game.play(0)

        self.assertEqual(game.board[0], "X")

    def test_should_be_O_turn_when_after_x_play_at_0(self):
        game = Game()

        game.start()
        game.play(0)

        self.assertEqual(game.turn, "O")
        self.assertEqual(game.board[0], "X")

    def test_should_block_1_is_O_and_then_X_turn_when_O_play_at_1(self):
        game = Game()

        game.start()
        game.play(0)
        game.play(1)

        self.assertEqual(game.turn, "X")
        self.assertEqual(game.board[0], "X")
        self.assertEqual(game.board[1], "O")

    def test_game_should_end_and_X_is_winner_when_X_take_3_vertical_block(self):
        game = Game()

        game.start()
        game.play(0)
        game.play(1)
        game.play(3)
        game.play(2)
        game.play(6)

        self.assertEqual(game.board[0], "X")
        self.assertEqual(game.board[3], "X")
        self.assertEqual(game.board[6], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_second_3_vertical_block(self):
        game = Game()

        game.start()
        game.play(1)
        game.play(3)
        game.play(4)
        game.play(2)
        game.play(7)

        self.assertEqual(game.board[1], "X")
        self.assertEqual(game.board[4], "X")
        self.assertEqual(game.board[7], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_third_3_vertical_block(self):
        game = Game()

        game.start()
        game.play(2)
        game.play(3)
        game.play(5)
        game.play(1)
        game.play(8)

        self.assertEqual(game.board[2], "X")
        self.assertEqual(game.board[5], "X")
        self.assertEqual(game.board[8], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_3_horizontal_block(self):
        game = Game()

        game.start()
        game.play(0)
        game.play(3)
        game.play(1)
        game.play(4)
        game.play(2)

        self.assertEqual(game.board[0], "X")
        self.assertEqual(game.board[1], "X")
        self.assertEqual(game.board[2], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_3_second_horizontal_block(
        self,
    ):
        game = Game()

        game.start()
        game.play(3)
        game.play(1)
        game.play(4)
        game.play(2)
        game.play(5)

        self.assertEqual(game.board[3], "X")
        self.assertEqual(game.board[4], "X")
        self.assertEqual(game.board[5], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_3_third_horizontal_block(
        self,
    ):
        game = Game()

        game.start()
        game.play(6)
        game.play(1)
        game.play(7)
        game.play(2)
        game.play(8)

        self.assertEqual(game.board[6], "X")
        self.assertEqual(game.board[7], "X")
        self.assertEqual(game.board[8], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_3_diagonal_block(self):
        game = Game()

        game.start()
        game.play(0)
        game.play(3)
        game.play(4)
        game.play(2)
        game.play(8)

        self.assertEqual(game.board[0], "X")
        self.assertEqual(game.board[4], "X")
        self.assertEqual(game.board[8], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_X_is_winner_when_X_take_another_3_diagonal_block(self):
        game = Game()

        game.start()
        game.play(2)
        game.play(3)
        game.play(4)
        game.play(1)
        game.play(6)

        self.assertEqual(game.board[2], "X")
        self.assertEqual(game.board[4], "X")
        self.assertEqual(game.board[6], "X")
        self.assertEqual(game.state, "X IS WINNER")

    def test_game_should_end_and_O_is_winner_when_O_take_another_3_diagonal_block(self):
        game = Game()

        game.start()
        game.play(3)
        game.play(2)
        game.play(1)
        game.play(4)
        game.play(5)
        game.play(6)

        self.assertEqual(game.board[2], "O")
        self.assertEqual(game.board[4], "O")
        self.assertEqual(game.board[6], "O")
        self.assertEqual(game.state, "O IS WINNER")

    def test_game_should_end_and_O_is_winner_when_O_take_another_3_diagonal_block(self):
        game = Game()

        game.start()
        game.play(2)
        game.play(2)

        self.assertEqual(game.board[2], "X")
        self.assertEqual(game.turn, "O")
        self.assertEqual(game.state, "O PLAYER CAN NOT PLAY IN FILLED BLOCK")


if __name__ == "__main__":
    unittest.main()
