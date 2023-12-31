from enum import Enum


class Codes(Enum):
    QUIT = -1
    RUNNING = 0
    MAIN_MENU = 1
    WINNER = 1
    PLAYER_VS_PLAYER = 2
    PLAYER_VS_COMPUTER = 3
    COMPUTER_VS_COMPUTER = 4
    TRAIN_COMPUTER = 5
