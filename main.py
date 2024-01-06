from codes import Codes
from connect_four_guis import ConnectFourGui, MainMenuGui


def connect_four_game(mode="pvp", player1_name="Player 1", player2_name="Player 2") -> int:
    connect_four = ConnectFourGui(
        player1_name=player1_name, player2_name=player2_name, mode=mode
    )
    return connect_four.start()


def main_menu() -> int:
    main_menu = MainMenuGui()
    return main_menu.start()


def main() -> None:
    code = Codes.MAIN_MENU
    while True:
        if code == Codes.MAIN_MENU:
            code = main_menu()
        elif code == Codes.PLAYER_VS_PLAYER:
            code = connect_four_game(
                mode="pvp", player1_name="Player 1", player2_name="Player 2"
            )
        elif code == Codes.PLAYER_VS_COMPUTER:
            return
        elif code == Codes.COMPUTER_VS_COMPUTER:
            return
        elif code == Codes.TRAIN_COMPUTER:
            return
        elif code == Codes.QUIT:
            return


if __name__ == "__main__":
    main()
    quit()
