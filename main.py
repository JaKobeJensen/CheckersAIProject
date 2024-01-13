from codes import Codes
from connect_four_guis import ConnectFourGui, MainMenuGui, ComputerSelectionGui


def connect_four_game(mode: str="pvp", player1_name: str="Player 1", player2_name: str="Player 2", computer_difficulty: str=None) -> Codes:
    connect_four = ConnectFourGui(
        player1_name=player1_name, player2_name=player2_name, mode=mode, computer_difficulty=computer_difficulty
    )
    return connect_four.start()


def computer_selection() -> Codes:
    computer_selection = ComputerSelectionGui()
    code = computer_selection.start()
    if code == Codes.EASY_MODE:
        return connect_four_game(
            mode="pvc", player1_name="Player 1", player2_name="Easy Computer", computer_difficulty="easy"
        )
    elif code == Codes.NORMAL_MODE:
        return connect_four_game(
            mode="pvc", player1_name="Player 1", player2_name="Normal Computer", computer_difficulty="normal"
        )
    elif code == Codes.HARD_MODE:
        return connect_four_game(
            mode="pvc", player1_name="Player 1", player2_name="Hard Computer", computer_difficulty="hard"
        )
    elif code == Codes.MASTER_MODE:
        return connect_four_game(
            mode="pvc", player1_name="Player 1", player2_name="Master Computer", computer_difficulty="master"
        )
    elif code == Codes.LOAD_COMPUTER:
        return Codes.RUNNING
    elif code == Codes.BACK:
        return Codes.MAIN_MENU
    else:
        return Codes.QUIT


def main_menu() -> Codes:
    main_menu = MainMenuGui()
    code = main_menu.start()
    if code == Codes.PLAYER_VS_PLAYER:
        return connect_four_game(
            mode="pvp", player1_name="Player 1", player2_name="Player 2"
        )
    elif code == Codes.PLAYER_VS_COMPUTER:
        return computer_selection()
    elif code == Codes.COMPUTER_VS_COMPUTER:
        return Codes.RUNNING
    elif code == Codes.TRAIN_COMPUTER:
        return Codes.RUNNING
    elif code == Codes.QUIT:
        return Codes.QUIT


def main() -> None:
    code = Codes.MAIN_MENU
    while True:
        if code == Codes.MAIN_MENU:
            code = main_menu()
        elif code == Codes.QUIT:
            return


if __name__ == "__main__":
    main()
    quit()
