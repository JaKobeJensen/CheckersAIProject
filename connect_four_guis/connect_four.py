import pygame
from pygame import Surface, display
from pygame.event import Event
from pygame.font import SysFont
from pygame.time import Clock

from codes import Codes
from connect_four import ConnectFour
from connect_four_guis.const import *
from connect_four_objects import GameBoard, RedPiece, YellowPiece
from gui_components import BoundingBoxObject, Screen, TextObject


class ConnectFourGui:
    PLAYER_NAMES_SIZE = 32

    def __init__(
        self, player1_name: str, player2_name: str, scaling_factor: float = 1.0
    ) -> None:
        self.display: Surface = display.set_mode(
            (
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
                round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
            )
        )
        self.screen: Screen = Screen(
            width=round(DEFAULT_DISPLAY_SIZE[0] * scaling_factor),
            height=round(DEFAULT_DISPLAY_SIZE[1] * scaling_factor),
        )
        self.connect_four = ConnectFour(player1_name, player2_name)
        self.game_object_id: dict[str, int] = {}
        self.scaling_factor = scaling_factor
        self.clock = Clock()

        """PLAYER1 NAME TEXT"""
        player1_name_text = TextObject(
            name="player1NameTxt",
            text=player1_name,
            text_font=SysFont(
                DEFAULT_FONT_TYPE, round(self.PLAYER_NAMES_SIZE * scaling_factor)
            ),
        )
        player1_name_text.position = (
            round(self.screen.width * 0.02),
            round(self.screen.height * 0.02),
        )
        self.game_object_id[player1_name_text.name] = len(self.screen.game_objects)
        self.screen.game_objects.add(player1_name_text)

        """PLAYER2 NAME TEXT"""
        player2_name_text = TextObject(
            name="player2NameTxt",
            text=player2_name,
            text_font=SysFont(
                DEFAULT_FONT_TYPE, round(self.PLAYER_NAMES_SIZE * scaling_factor)
            ),
        )
        player2_name_text.position = (
            round(
                (self.screen.width - player2_name_text.width)
                - (self.screen.height * 0.02)
            ),
            round(self.screen.width * 0.02),
        )
        self.game_object_id[player2_name_text.name] = len(self.screen.game_objects)
        self.screen.game_objects.add(player2_name_text)

        """PLAYER 1 PIECE INDICATOR"""
        player1_piece_indicator = RedPiece("player1Indicator")
        player1_piece_indicator.position = (
            round(player1_name_text.rect.right + (10 * scaling_factor)),
            round(player1_name_text.y),
        )
        self.game_object_id[player1_piece_indicator.name] = len(
            self.screen.game_objects
        )
        self.screen.game_objects.add(player1_piece_indicator)

        """PLAYER 2 PIECE INDICATOR"""
        player2_piece_indicator = YellowPiece("player2Indicator")
        player2_piece_indicator.position = (
            round(
                player2_name_text.rect.left
                - player2_piece_indicator.width
                - (10 * scaling_factor)
            ),
            round(player2_name_text.y),
        )
        self.game_object_id[player2_piece_indicator.name] = len(
            self.screen.game_objects
        )
        self.screen.game_objects.add(player2_piece_indicator)

        """CONNECT FOUR BOARD"""
        connect_four_board = GameBoard(name="gameboard")
        connect_four_board.position = (
            round(self.screen.width / 2 - connect_four_board.width / 2),
            round(
                (self.screen.height - connect_four_board.height)
                - (self.screen.height * 0.05)
            ),
        )
        self.game_object_id[connect_four_board.name] = len(self.screen.game_objects)
        self.screen.game_objects.add(connect_four_board)

        """BOUNDING BOX OBJECTS"""
        for i in range(7):
            column_bounding_box = BoundingBoxObject(
                name="column{0}Bbx".format(i),
                width=round(connect_four_board.width / 7),
                height=connect_four_board.height,
                visible=False,
            )
            column_bounding_box.position = (
                round((column_bounding_box.width * i) + connect_four_board.x),
                connect_four_board.y,
            )
            self.game_object_id[column_bounding_box.name] = len(
                self.screen.game_objects
            )
            self.screen.game_objects.add(column_bounding_box)
        bottom_bounding_box = BoundingBoxObject(
            name="bottomBbx",
            width=self.screen.width,
            height=10,
            visible=False,
        )
        bottom_bounding_box.position = (
            0,
            connect_four_board.rect.bottom,
        )
        self.game_object_id[bottom_bounding_box.name] = len(self.screen.game_objects)
        self.screen.game_objects.add(bottom_bounding_box)

        return

    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
        return Codes.RUNNING

    def start(self) -> Codes:
        code = Codes.RUNNING
        while code is Codes.RUNNING:
            for event in pygame.event.get():
                code = self._event_check(event)
            self.screen.update()
            self.display.blit(
                self.screen.screen,
                (self.screen.x, self.screen.y),
            )
            display.update()
            self.clock.tick(DEFAULT_FRAMERATE)
        return code
