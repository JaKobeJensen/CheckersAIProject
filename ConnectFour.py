
class ConnectFour:
    GAMEBOARD_WIDTH = 7
    GAMEBOARD_HEIGHT = 6

    def __init__(self, player1Name:str="", player2Name:str=""):
        self.gameBoard:list[list[int]] = [[0 for _ in range(self.GAMEBOARD_WIDTH)] for _ in range(self.GAMEBOARD_HEIGHT)]
        self._gameBoard:list[list[int]] = [[0 for _ in range(self.GAMEBOARD_WIDTH)] for _ in range(self.GAMEBOARD_HEIGHT)]
        self.__gameBoard:list[list[int]] = [[0 for _ in range(self.GAMEBOARD_WIDTH)] for _ in range(self.GAMEBOARD_HEIGHT)]
        self.player1Turn:bool = True
        self.player1Name = player1Name
        self.player2Name = player2Name

    def get_gameboard(self)->list[list[int]]:
        return self.__gameBoard


connectFour = ConnectFour()
quit()