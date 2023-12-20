class ConnectFour:
    GAMEBOARD_WIDTH = 7
    GAMEBOARD_HEIGHT = 6
    EMPTY_SPACE = 0
    PLAYER1_SPACE = 1
    PLAYER2_SPACE = -1

    def __init__(self, player1Name:str="", player2Name:str=""):
        self._gameBoard:list[list[int]] = [[self.EMPTY_SPACE for _ in range(self.GAMEBOARD_WIDTH)] for _ in range(self.GAMEBOARD_HEIGHT)]
        self._player1Turn:bool = True
        self._winner:str = None
        self.player1Name:str = player1Name
        self.player2Name:str = player2Name

    def _check_win(self)->None:
        for rowIdx, row in enumerate(self._gameBoard):
            for colIdx, space in enumerate(row):
                if not self._check_win_rec((rowIdx,colIdx), space, 0):
                    continue
                if space == self.PLAYER1_SPACE:
                    self._winner = self.player1Name
                else:
                    self._winner = self.player2Name
                return
        return        

    def _check_win_rec(self, idx:tuple[int,int], prevSpace:int, layer:int, direction:str="all")->bool:
        if layer == 4:
            return True
        if (direction == "all" and prevSpace == self.EMPTY_SPACE or
                idx[0] < 0 or idx[0] >= self.GAMEBOARD_HEIGHT or
                idx[1] < 0 or idx[1] >= self.GAMEBOARD_WIDTH or
                prevSpace != self._gameBoard[idx[0]][idx[1]]):
            return False
        #if ((direction == "left" or direction == "all") and 
        #        self._check_win_rec((idx[0],idx[1]-1), self._gameBoard[idx[0]][idx[1]], layer+1, "left")):
        #    return True
        if ((direction == "right" or direction == "all") and 
                self._check_win_rec((idx[0],idx[1]+1), self._gameBoard[idx[0]][idx[1]], layer+1, "right")):
            return True
        #if ((direction == "up" or direction == "all") and 
        #        self._check_win_rec((idx[0]-1,idx[1]), self._gameBoard[idx[0]][idx[1]], layer+1, "up")):
        #    return True
        if ((direction == "down" or direction == "all") and 
                self._check_win_rec((idx[0]+1,idx[1]), self._gameBoard[idx[0]][idx[1]], layer+1, "down")):
            return True
        #if ((direction == "upleft" or direction == "all") and 
        #        self._check_win_rec((idx[0]-1,idx[1]-1), self._gameBoard[idx[0]][idx[1]], layer+1, "upleft")):
        #    return True
        #if ((direction == "upright" or direction == "all") and 
        #        self._check_win_rec((idx[0]-1,idx[1]+1), self._gameBoard[idx[0]][idx[1]], layer+1, "upright")):
        #    return True
        if ((direction == "downleft" or direction == "all") and 
                self._check_win_rec((idx[0]+1,idx[1]-1), self._gameBoard[idx[0]][idx[1]], layer+1, "downleft")):
            return True
        if ((direction == "downright" or direction == "all") and 
                self._check_win_rec((idx[0]+1,idx[1]+1), self._gameBoard[idx[0]][idx[1]], layer+1, "downright")):
            return True
        return False

    def get_gameboard(self)->list[list[int]]:
        return self._gameBoard
    
    def get_winner(self)->str:
        return self._winner

    def whos_turn(self)->str:
        if self._player1Turn: return self.player1Name
        else: return self.player2Name

    def reset_board(self)->None:
        self._gameBoard = [[self.EMPTY_SPACE for _ in range(self.GAMEBOARD_WIDTH)] for _ in range(self.GAMEBOARD_HEIGHT)]
        self._player1Turn = True
        self._winner = None

    def player_move(self, column:int)->bool:
        if self._winner != None:
            return False
        column -= 1
        for row in reversed(range(len(self._gameBoard))):
            if self._gameBoard[row][column] != self.EMPTY_SPACE:
                continue
            if self._player1Turn:
                self._gameBoard[row][column] = self.PLAYER1_SPACE
                self._player1Turn = False
            else:
                self._gameBoard[row][column] = self.PLAYER2_SPACE
                self._player1Turn = True
            self._check_win()
            return True
        return False