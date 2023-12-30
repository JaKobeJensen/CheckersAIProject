import pygame

from gui_components import PictureBoxObject


class YellowPiece(PictureBoxObject):
    IAMGE_PATH = "connect_four_images\\yellow_connect_four_piece.png"

    def __init__(
        self,
        name: str,
        position: tuple[int, int] = (0, 0),
        visible: bool = True,
    ) -> None:
        image = pygame.image.load(self.IAMGE_PATH)
        PictureBoxObject.__init__(
            self,
            name=name,
            image=image,
            position=position,
            visible=visible,
        )
        return


class RedPiece(PictureBoxObject):
    IAMGE_PATH = "connect_four_images\\red_connect_four_piece.png"

    def __init__(
        self,
        name: str,
        position: tuple[int, int] = (0, 0),
        visible: bool = True,
    ) -> None:
        image = pygame.image.load(self.IAMGE_PATH)
        PictureBoxObject.__init__(
            self,
            image=image,
            name=name,
            position=position,
            visible=visible,
        )
        return


class GameBoard(PictureBoxObject):
    IAMGE_PATH = "connect_four_images\\connect_four_board.png"

    def __init__(
        self,
        name: str,
        position: tuple[int, int] = (0, 0),
        visible: bool = True,
    ) -> None:
        image = pygame.image.load(self.IAMGE_PATH)
        PictureBoxObject.__init__(
            self,
            name=name,
            image=image,
            position=position,
            visible=visible,
        )
        return
