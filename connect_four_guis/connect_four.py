import pygame
from pygame import Surface, display, transform
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
    PLAYER_PIECE_INDICATOR_SCALING = 0.4

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
            width=DEFAULT_DISPLAY_SIZE[0],
            height=DEFAULT_DISPLAY_SIZE[1],
            screen_scaling_factor=scaling_factor,
        )
        self.connect_four = ConnectFour(player1_name, player2_name)
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.scaling_factor: float = scaling_factor
        self.clock: Clock = Clock()
        self._current_column: int = 0

        self.screen.add_new_group("static_objects")
        self.screen.add_new_group("played_pieces")
        self.screen.add_new_group("chooser_pieces")
        self.screen.add_new_group("column_bounding_boxes")

        """PLAYER1 NAME TEXT"""
        player1_name_text = TextObject(
            name="player1NameTxt",
            text=player1_name,
            text_font=SysFont(DEFAULT_FONT_TYPE, self.PLAYER_NAMES_SIZE),
            scaling_factor=scaling_factor,
        )
        player1_name_text.position = (
            round(self.screen.width * 0.02),
            round(self.screen.height * 0.02),
        )
        self.screen.groups["static_objects"].add(player1_name_text)

        """PLAYER2 NAME TEXT"""
        player2_name_text = TextObject(
            name="player2NameTxt",
            text=player2_name,
            text_font=SysFont(DEFAULT_FONT_TYPE, self.PLAYER_NAMES_SIZE),
            scaling_factor=scaling_factor,
        )
        player2_name_text.position = (
            round(
                (self.screen.width - player2_name_text.width)
                - (self.screen.height * 0.02)
            ),
            round(self.screen.width * 0.02),
        )
        self.screen.groups["static_objects"].add(player2_name_text)

        """PLAYER 1 PIECE INDICATOR"""
        player1_piece_indicator = RedPiece(
            name="player1Indicator",
            scaling_factor=scaling_factor * self.PLAYER_PIECE_INDICATOR_SCALING,
        )
        player1_piece_indicator.position = (
            round(player1_name_text.rect.right + player1_piece_indicator.width * 0.5),
            round(
                player1_name_text.y
                - (player1_piece_indicator.height - player1_name_text.height)
            ),
        )
        self.screen.groups["static_objects"].add(player1_piece_indicator)

        """PLAYER 2 PIECE INDICATOR"""
        player2_piece_indicator = YellowPiece(
            name="player2Indicator",
            scaling_factor=scaling_factor * self.PLAYER_PIECE_INDICATOR_SCALING,
        )
        player2_piece_indicator.position = (
            round(
                player2_name_text.rect.left
                - player2_piece_indicator.width
                - player2_piece_indicator.width * 0.5
            ),
            round(
                player2_name_text.y
                - (player2_piece_indicator.height - player2_name_text.height)
            ),
        )
        self.screen.groups["static_objects"].add(player2_piece_indicator)

        """CONNECT FOUR BOARD"""
        connect_four_board = GameBoard(name="gameboard", scaling_factor=scaling_factor)
        connect_four_board.position = (
            round(self.screen.width / 2 - connect_four_board.width / 2),
            round(
                (self.screen.height - connect_four_board.height)
                - (self.screen.height * 0.05)
            ),
        )
        self.screen.groups["static_objects"].add(connect_four_board)

        """RED PIECE CHOOSER"""
        red_piece_chooser = RedPiece(
            name="redPieceChooser", scaling_factor=scaling_factor, visible=True
        )
        red_piece_chooser.position = (
            connect_four_board.x,
            connect_four_board.y
            - red_piece_chooser.height
            - round(red_piece_chooser.height * 0.3),
        )
        self.screen.groups["chooser_pieces"].add(red_piece_chooser)

        """YELLOW PIECE CHOOSER"""
        yellow_piece_chooser = YellowPiece(
            name="redPieceChooser", scaling_factor=scaling_factor, visible=False
        )
        yellow_piece_chooser.position = (
            connect_four_board.x,
            connect_four_board.y
            - yellow_piece_chooser.height
            - round(yellow_piece_chooser.height * 0.3),
        )
        self.screen.groups["chooser_pieces"].add(yellow_piece_chooser)

        """BOUNDING BOX OBJECTS"""
        for i in range(7):
            column_bounding_box = BoundingBoxObject(
                name="column{0}Bbx".format(i),
                width=round(connect_four_board.width / 7),
                height=self.screen.height,
                scaling_factor=scaling_factor,
                visible=False,
            )
            column_bounding_box.position = (
                round((column_bounding_box.width * i) + connect_four_board.x),
                0,
            )
            self.screen.groups["column_bounding_boxes"].add(column_bounding_box)
        bottom_bounding_box = BoundingBoxObject(
            name="bottomBbx",
            width=self.screen.width,
            height=10,
            scaling_factor=scaling_factor,
            visible=False,
        )
        bottom_bounding_box.position = (
            0,
            connect_four_board.rect.bottom,
        )

        return

    def _event_check(self, event: Event) -> Codes:
        if event.type == pygame.QUIT:
            return Codes.QUIT
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._drop_piece()
            self._check_winner()
        return Codes.RUNNING

    def _mouse_hover_column_bounding_box_check(self) -> None:
        for column_index, column in enumerate(
            self.screen.groups["column_bounding_boxes"]
        ):
            if column.move_hover():
                for chooser in self.screen.groups["chooser_pieces"]:
                    chooser.x = round(column.x + (column.width / 2 - chooser.width / 2))
                    self._current_column = column_index
        return

    def _drop_piece(self) -> None:
        if self.connect_four.winner is None:
            self.connect_four.player_move(self._current_column)
            if self.connect_four.whos_turn == self.player2_name:
                new_piece = RedPiece(
                    name="redPiece{0}".format(
                        int(self.connect_four.number_of_moves - 1 / 2)
                    ),
                    scaling_factor=self.scaling_factor,
                    visible=True,
                )
                self.screen.groups["chooser_pieces"].get_sprite(0).visible = False
                self.screen.groups["chooser_pieces"].get_sprite(1).visible = True
            else:
                new_piece = YellowPiece(
                    name="yellowPiece{0}".format(
                        round(self.connect_four.number_of_moves - 1 / 2)
                    ),
                    scaling_factor=self.scaling_factor,
                    visible=True,
                )
                self.screen.groups["chooser_pieces"].get_sprite(0).visible = True
                self.screen.groups["chooser_pieces"].get_sprite(1).visible = False
            new_piece.position = (
                self.screen.groups["chooser_pieces"].get_top_sprite().x,
                self.screen.groups["static_objects"]
                .get_sprite(len(self.screen.groups["static_objects"]) - 1)
                .y
                + round(
                    self.screen.groups["static_objects"]
                    .get_sprite(len(self.screen.groups["static_objects"]) - 1)
                    .height
                    / 6
                )
                * self.connect_four.last_piece_played_position()[0],
            )
            self.screen.groups["played_pieces"].add(new_piece)

    def _check_winner(self) -> None:
        if self.connect_four.winner is None:
            return
        self.screen.groups["chooser_pieces"].get_sprite(0).visible = False
        self.screen.groups["chooser_pieces"].get_sprite(1).visible = False
        winner_text = TextObject(
            name="player1NameTxt",
            text="{0} Wins".format(self.connect_four.winner),
            text_font=SysFont(DEFAULT_FONT_TYPE, 128),
            scaling_factor=self.scaling_factor,
        )
        winner_text.position = (
            round(self.screen.width / 2 - winner_text.width / 2),
            round(self.screen.height * 0.1),
        )
        self.screen.groups["static_objects"].add(winner_text)

    def start(self) -> Codes:
        code = Codes.RUNNING
        while code is Codes.RUNNING:
            for event in pygame.event.get():
                code = self._event_check(event)

            self._mouse_hover_column_bounding_box_check()

            self.screen.update()
            self.display.blit(
                self.screen.screen,
                (self.screen.x, self.screen.y),
            )
            display.update()
            self.clock.tick(DEFAULT_FRAMERATE)
        return code
