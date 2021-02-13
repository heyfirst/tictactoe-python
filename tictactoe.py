class Game:
    board = []
    turn = ""
    state = ""

    def __init__(self) -> None:
        self.board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    def start(self):
        self.turn = "X"
        self.state = f"{self.turn} TURN"

    def play(self, position):
        if self.board[position] != "_":
            self.state = f"{self.turn} PLAYER CAN NOT PLAY IN FILLED BLOCK"
            return

        self.board[position] = self.turn

        if self._check_win():
            return

        if self.turn is "X":
            self.turn = "O"
        else:
            self.turn = "X"

        self.state = f"{self.turn} TURN"

    def _check_win(self):
        if (
            (
                self.board[0] == self.turn
                and self.board[3] == self.turn
                and self.board[6] == self.turn
            )
            or (
                self.board[1] == self.turn
                and self.board[4] == self.turn
                and self.board[7] == self.turn
            )
            or (
                self.board[2] == self.turn
                and self.board[5] == self.turn
                and self.board[8] == self.turn
            )
            or (
                self.board[0] == self.turn
                and self.board[1] == self.turn
                and self.board[2] == self.turn
            )
            or (
                self.board[3] == self.turn
                and self.board[4] == self.turn
                and self.board[5] == self.turn
            )
            or (
                self.board[6] == self.turn
                and self.board[7] == self.turn
                and self.board[8] == self.turn
            )
            or (
                self.board[0] == self.turn
                and self.board[4] == self.turn
                and self.board[8] == self.turn
            )
            or (
                self.board[2] == self.turn
                and self.board[4] == self.turn
                and self.board[6] == self.turn
            )
        ):
            self.state = f"{self.turn} IS WINNER"
            return True
