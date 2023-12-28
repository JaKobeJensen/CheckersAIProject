from codes import Codes
from connect_four_guis import MainMenuGui


def main():
    main_menu_gui = MainMenuGui()
    code = main_menu_gui.start()
    if code is Codes.QUIT:
        quit()
    elif code is Codes.PLAYER_VS_PLAYER:
        print("Player VS Player Button was pressed")
    elif code is Codes.PLAYER_VS_COMPUTER:
        print("Player VS Computer Button was pressed")
    elif code is Codes.COMPUTER_VS_COMPUTER:
        print("Computer VS Computer Button was pressed")
    elif code is Codes.TRAIN_COMPUTER:
        print("Train Computer Button was pressed")
    return


if __name__ == "__main__":
    main()
    quit()
