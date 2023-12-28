from enum import Enum


class Codes(Enum):
    QUIT = -1
    RUNNING = 0
    PLAYER_VS_PLAYER = 1
    PLAYER_VS_COMPUTER = 2
    COMPUTER_VS_COMPUTER = 3
    TRAIN_COMPUTER = 4
