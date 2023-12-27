class ConnectFour:
    GAMEBOARD_WIDTH = 7
    GAMEBOARD_HEIGHT = 6
    EMPTY_SPACE = 0
    PLAYER1_SPACE = 1
    PLAYER2_SPACE = -1

    def __init__(self, player1_name: str = "", player2_name: str = "") -> None:
        self._game_board: list[list[int]] = [
            [self.EMPTY_SPACE for _ in range(self.GAMEBOARD_WIDTH)]
            for _ in range(self.GAMEBOARD_HEIGHT)
        ]
        self._player1_turn: bool = True
        self._winner: str = None
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        return

    @property
    def game_board(self) -> list[list[int]]:
        return self._game_board.copy()

    @property
    def winner(self) -> str | None:
        return self._winner

    @property
    def whos_turn(self) -> str:
        if self._player1_turn:
            return self.player1_name
        else:
            return self.player2_name

    def _check_win(self) -> None:
        for rowIdx, row in enumerate(self._game_board):
            for colIdx, space in enumerate(row):
                if not self._check_win_rec((rowIdx, colIdx), space, 0):
                    continue
                if space == self.PLAYER1_SPACE:
                    self._winner = self.player1_name
                else:
                    self._winner = self.player2_name
                return
        return

    def _check_win_rec(
        self,
        idx: tuple[int, int],
        previous_space: int,
        layer: int,
        direction: str = "all",
    ) -> bool:
        if layer == 4:
            return True
        if (
            direction == "all"
            and previous_space == self.EMPTY_SPACE
            or idx[0] < 0
            or idx[0] >= self.GAMEBOARD_HEIGHT
            or idx[1] < 0
            or idx[1] >= self.GAMEBOARD_WIDTH
            or previous_space != self._game_board[idx[0]][idx[1]]
        ):
            return False
        if (direction == "right" or direction == "all") and self._check_win_rec(
            (idx[0], idx[1] + 1), self._game_board[idx[0]][idx[1]], layer + 1, "right"
        ):
            return True
        if (direction == "down" or direction == "all") and self._check_win_rec(
            (idx[0] + 1, idx[1]), self._game_board[idx[0]][idx[1]], layer + 1, "down"
        ):
            return True
        if (direction == "downleft" or direction == "all") and self._check_win_rec(
            (idx[0] + 1, idx[1] - 1),
            self._game_board[idx[0]][idx[1]],
            layer + 1,
            "downleft",
        ):
            return True
        if (direction == "downright" or direction == "all") and self._check_win_rec(
            (idx[0] + 1, idx[1] + 1),
            self._game_board[idx[0]][idx[1]],
            layer + 1,
            "downright",
        ):
            return True
        return False

    def reset_board(self) -> None:
        self._game_board = [
            [self.EMPTY_SPACE for _ in range(self.GAMEBOARD_WIDTH)]
            for _ in range(self.GAMEBOARD_HEIGHT)
        ]
        self._player1_turn = True
        self._winner = None
        return

    def player_move(self, column: int) -> bool:
        if self._winner is None:
            return False
        column -= 1
        for row in reversed(range(len(self._game_board))):
            if self._game_board[row][column] != self.EMPTY_SPACE:
                continue
            if self._player1_turn:
                self._game_board[row][column] = self.PLAYER1_SPACE
                self._player1Turn = False
            else:
                self._game_board[row][column] = self.PLAYER2_SPACE
                self._player1_turn = True
            self._check_win()
            return True
        return False
