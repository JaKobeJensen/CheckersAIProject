import copy
import random

from connect_four import ConnectFour


class MinimaxConnectFourAI:
    _EASY_DEPTH: int = 1
    _NORMAL_DEPTH: int = 3
    _HARD_DEPTH: int = 5
    _MASTER_DEPTH: int = 7

    _HEAT_MAP = [
        [10, 20, 30, 40, 30, 20, 10],
        [10, 20, 30, 40, 30, 20, 10],
        [10, 20, 30, 40, 30, 20, 10],
        [10, 20, 30, 40, 30, 20, 10],
        [10, 20, 30, 40, 30, 20, 10],
        [10, 20, 30, 40, 30, 20, 10],
    ]

    def __init__(self, name: str, piece_color: int, difficulty: str = "normal") -> None:
        self._name: str = name
        self._piece_color: int = piece_color
        self.difficulty: str = difficulty
        return

    @property
    def name(self) -> str:
        return self._name

    def _mininmax(self, game_state: ConnectFour, depth: int) -> float:
        alpha = -float("inf")
        beta = float("inf")
        best_move = random.choice(game_state.legal_moves())
        best_value = -float("inf")
        for move in game_state.legal_moves():
            game_state_copy = copy.deepcopy(game_state)
            game_state_copy.player_move(move)
            value = self._minimax_rec(game_state_copy, depth - 1, alpha, beta, False)
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
            if best_value >= beta:
                break
        return best_move

    def _minimax_rec(
        self,
        game_state: ConnectFour,
        depth: int,
        alpha: float,
        beta: float,
        maximizing_player: bool,
    ) -> int:
        if depth == 0 or game_state.winner is not None:
            return self._heuristic_function(game_state)

        if maximizing_player:
            value = -float("inf")
            for move in game_state.legal_moves():
                game_state_copy = copy.deepcopy(game_state)
                game_state_copy.player_move(move)
                value = max(
                    value,
                    self._minimax_rec(game_state_copy, depth - 1, alpha, beta, False),
                )
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return value
        else:
            value = float("inf")
            for move in game_state.legal_moves():
                game_state_copy = copy.deepcopy(game_state)
                game_state_copy.player_move(move)
                value = min(
                    value,
                    self._minimax_rec(game_state_copy, depth - 1, alpha, beta, True),
                )
                beta = min(beta, value)
                if value <= alpha:
                    break
            return value

    def _heuristic_function(self, game_state: ConnectFour) -> float:
        if game_state.winner is not None and game_state.winner == self._name:
            return float("inf")
        elif game_state.winner is not None and game_state.winner != self._name:
            return -float("inf")

        heuristic_value: float = 0

        for row_idx, row in enumerate(game_state.game_board):
            for col_idx, space in enumerate(row):
                heuristic_value += (
                    space * self._HEAT_MAP[row_idx][col_idx] * self._piece_color
                )

        return heuristic_value

    def move(self, game_state: ConnectFour) -> int:
        if self.difficulty == "easy":
            return self._mininmax(game_state, self._EASY_DEPTH)
        elif self.difficulty == "normal":
            return self._mininmax(game_state, self._NORMAL_DEPTH)
        elif self.difficulty == "hard":
            return self._mininmax(game_state, self._HARD_DEPTH)
        elif self.difficulty == "master":
            return self._mininmax(game_state, self._MASTER_DEPTH)
        else:
            return None
